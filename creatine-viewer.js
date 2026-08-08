import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

const wrap = document.getElementById('wrap');
const loading = document.getElementById('loading');
const progress = document.getElementById('loading-fill');
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(wrap.clientWidth, wrap.clientHeight);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 0.9;
wrap.prepend(renderer.domElement);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(34, wrap.clientWidth / wrap.clientHeight, 0.01, 100);
const controls = new OrbitControls(camera, renderer.domElement);
controls.enablePan = false;
controls.enableDamping = true;
controls.autoRotate = true;
controls.autoRotateSpeed = 0.72;
controls.minDistance = 3.3;
controls.maxDistance = 7.0;
controls.minPolarAngle = Math.PI / 2 - 0.52;
controls.maxPolarAngle = Math.PI / 2 + 0.52;

scene.add(new THREE.HemisphereLight(0xffffff, 0x1f242d, 1.15));
const key = new THREE.DirectionalLight(0xfffdf9, 2.05); key.position.set(3.5, 5.5, 5); scene.add(key);
const fill = new THREE.DirectionalLight(0xd8efff, 0.72); fill.position.set(-4, 2, 3); scene.add(fill);
const rim = new THREE.DirectionalLight(0x8eeeff, 0.92); rim.position.set(2, 1, -4); scene.add(rim);

const loader = new GLTFLoader();
loader.load('./creatine-300g.glb?v=20260808-stable2', (gltf) => {
  const model = gltf.scene;
  const maxAnisotropy = Math.min(16, renderer.capabilities.getMaxAnisotropy());
  model.traverse((node) => {
    if (!node.isMesh || !node.material) return;
    const materials = Array.isArray(node.material) ? node.material : [node.material];
    materials.forEach((material) => {
      ['map', 'emissiveMap', 'normalMap', 'roughnessMap', 'metalnessMap', 'aoMap'].forEach((key) => {
        const map = material[key];
        if (!map) return;
        map.anisotropy = maxAnisotropy;
        if (key === 'map' || key === 'emissiveMap') map.colorSpace = THREE.SRGBColorSpace;
        map.needsUpdate = true;
      });
      if (/Exact_Creatine|Packaging/i.test(material.name)) {
        material.roughness = Math.max(material.roughness ?? 0, 0.5);
        material.metalness = 0;
        material.envMapIntensity = 0.58;
      }
      if (/Unprinted_Matte_Black/i.test(material.name)) {
        material.roughness = Math.max(material.roughness ?? 0, 0.48);
        material.envMapIntensity = 0.5;
      }
      material.needsUpdate = true;
    });
  });
  const box = new THREE.Box3().setFromObject(model);
  const center = box.getCenter(new THREE.Vector3());
  model.position.sub(center);
  scene.add(model);
  const size = new THREE.Box3().setFromObject(model).getSize(new THREE.Vector3());
  camera.position.set(0, size.y * 0.02, Math.max(size.x, size.y) * 1.95);
  controls.target.set(0, 0, 0); controls.update();
  loading.classList.add('is-hidden');
}, (e) => { if (e.total) progress.style.width = `${Math.round(e.loaded/e.total*100)}%`; }, () => loading.classList.add('is-hidden'));

function frame(){ requestAnimationFrame(frame); controls.update(); renderer.render(scene,camera); }
frame();
addEventListener('resize',()=>{camera.aspect=wrap.clientWidth/wrap.clientHeight;camera.updateProjectionMatrix();renderer.setSize(wrap.clientWidth,wrap.clientHeight);});
