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
renderer.toneMappingExposure = 1.08;
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

scene.add(new THREE.HemisphereLight(0xffffff, 0x313944, 2.4));
const key = new THREE.DirectionalLight(0xffffff, 4.3); key.position.set(3.5, 5.5, 5); scene.add(key);
const fill = new THREE.DirectionalLight(0xbfefff, 2.3); fill.position.set(-4, 2, 3); scene.add(fill);
const rim = new THREE.DirectionalLight(0x42dfee, 1.9); rim.position.set(2, 1, -4); scene.add(rim);

const loader = new GLTFLoader();
loader.load('./creatine-300g.glb', (gltf) => {
  const model = gltf.scene;
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
