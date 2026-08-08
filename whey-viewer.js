import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';

const wrap = document.getElementById('wrap');
const loading = document.getElementById('loading');
const progress = document.getElementById('loading-fill');
const labelUrl = document.body.dataset.label;

const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(wrap.clientWidth, wrap.clientHeight);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 0.92;
wrap.prepend(renderer.domElement);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(35, wrap.clientWidth / wrap.clientHeight, 0.01, 100);
camera.position.set(0, 0.04, 3.1);

const controls = new OrbitControls(camera, renderer.domElement);
controls.enablePan = false;
controls.enableDamping = true;
controls.autoRotate = true;
controls.autoRotateSpeed = 0.85;
controls.minDistance = 1.75;
controls.maxDistance = 4.2;
controls.minPolarAngle = Math.PI / 2 - 0.52;
controls.maxPolarAngle = Math.PI / 2 + 0.52;

scene.add(new THREE.HemisphereLight(0xffffff, 0x20242d, 1.2));
const key = new THREE.DirectionalLight(0xfffdf9, 2.15);
key.position.set(3.4, 4.8, 5.4);
scene.add(key);
const fill = new THREE.DirectionalLight(0xd8efff, 0.78);
fill.position.set(-4, 1.4, 3.2);
scene.add(fill);
const rim = new THREE.DirectionalLight(0xffe7bd, 0.95);
rim.position.set(2.2, 1.2, -4.5);
scene.add(rim);

const group = new THREE.Group();
scene.add(group);

const textureLoader = new THREE.TextureLoader();
const labelTexture = textureLoader.load(labelUrl);
labelTexture.colorSpace = THREE.SRGBColorSpace;
labelTexture.wrapS = THREE.ClampToEdgeWrapping;
labelTexture.wrapT = THREE.ClampToEdgeWrapping;
labelTexture.flipY = true;
labelTexture.anisotropy = Math.min(16, renderer.capabilities.getMaxAnisotropy());

const draco = new DRACOLoader();
draco.setDecoderPath('https://unpkg.com/three@0.160.0/examples/jsm/libs/draco/');
const loader = new GLTFLoader();
loader.setDRACOLoader(draco);

loader.load(
  './whey-2kg.glb',
  (gltf) => {
    const model = gltf.scene;
    model.traverse((node) => {
      if (!node.isMesh) return;
      node.material = new THREE.MeshPhysicalMaterial({
        color: 0x08090b,
        roughness: 0.42,
        metalness: 0.0,
        clearcoat: 0.24,
        clearcoatRoughness: 0.32
      });
    });

    const initialBox = new THREE.Box3().setFromObject(model);
    model.position.sub(initialBox.getCenter(new THREE.Vector3()));
    group.add(model);

    const box = new THREE.Box3().setFromObject(model);
    const size = box.getSize(new THREE.Vector3());
    const radius = Math.max(size.x, size.z) * 0.505;
    const labelHeight = (Math.PI * 2 * radius) / (4096 / 1164);
    const labelBottom = box.min.y + size.y * 0.105;

    const label = new THREE.Mesh(
      new THREE.CylinderGeometry(radius, radius, labelHeight, 160, 1, true),
      new THREE.MeshPhysicalMaterial({
        map: labelTexture,
        transparent: true,
        alphaTest: 0.015,
        roughness: 0.5,
        clearcoat: 0.08,
        side: THREE.FrontSide
      })
    );
    label.position.y = labelBottom + labelHeight / 2;
    label.rotation.y = Math.PI;
    group.add(label);

    camera.position.set(size.x * 0.04, size.y * 0.03, Math.max(size.x, size.y) * 2.85);
    controls.target.set(0, 0, 0);
    controls.update();
    loading.classList.add('is-hidden');
  },
  (event) => {
    if (event.total) progress.style.width = `${Math.round(event.loaded / event.total * 100)}%`;
  },
  () => loading.classList.add('is-hidden')
);

function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();

addEventListener('resize', () => {
  camera.aspect = wrap.clientWidth / wrap.clientHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(wrap.clientWidth, wrap.clientHeight);
});
