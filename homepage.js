import * as THREE from 'three';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';
import { DRACOLoader } from 'three/addons/loaders/DRACOLoader.js';

const ASSET_VERSION = '20260808-studio4';
const assetUrl = (path) => {
  const url = new URL(path, import.meta.url);
  url.searchParams.set('v', ASSET_VERSION);
  return url.href;
};

const products = [
  {
    id: 'omega3', name: 'OMEGA-3', series: 'CLINICAL SERIES',
    eyebrow: 'ΝΕΑ ΕΠΟΧΗ · B2H', title: 'Η ΥΓΕΙΑ ΣΑΣ,<br>ΣΕ ΚΙΝΗΣΗ.',
    description: 'Δέκα στοχευμένες φόρμουλες. Ένα νέο σύστημα καθημερινής υποστήριξης.',
    cta: 'ΓΝΩΡΙΣΤΕ ΤΗ ΝΕΑ ΣΕΙΡΑ', url: '#products', accent: '#d6b338', halo: 'rgba(255,255,255,.94)', theme: 'light',
    model: 'omega3_final.glb', label: 'label.png', type: 'bottle', flipY: true, radius: 1.018, labelAspect: 142 / 53, yStart: .07, seam: Math.PI / 2
  },
  {
    id: 'magnesium', name: 'MAGNESIUM', series: 'CLINICAL SERIES',
    eyebrow: 'ΚΑΘΗΜΕΡΙΝΗ ΥΠΟΣΤΗΡΙΞΗ', title: 'Η ΒΑΣΗ ΤΗΣ<br>ΙΣΟΡΡΟΠΙΑΣ.',
    description: 'Μια καθαρή, σύγχρονη προσέγγιση στη σταθερή καθημερινή σας ρουτίνα.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#5d45ad', halo: 'rgba(242,236,255,.94)', theme: 'light',
    model: 'magnesium_final.glb', label: 'magnesium-label.png', type: 'bottle', flipY: true, radius: 1.018, labelAspect: 142 / 53, yStart: .07, seam: Math.PI / 2,
    effects: [
      'home-assets/floaters/magnesium/magnesium-tablet-angle-01-front-three-quarter.png',
      'home-assets/floaters/magnesium/magnesium-tablet-angle-02-edge-profile.png',
      'home-assets/floaters/magnesium/magnesium-tablet-angle-03-near-top.png'
    ]
  },
  {
    id: 'multivitamin', name: 'BACK2VITAMIN', series: 'CLINICAL SERIES',
    eyebrow: 'Η ΚΑΘΗΜΕΡΙΝΗ ΣΑΣ ΒΑΣΗ', title: 'ΚΑΘΕ ΜΕΡΑ,<br>ΠΙΟ ΜΠΡΟΣΤΑ.',
    description: 'Η νέα καθημερινή βάση για ενέργεια, συνέπεια και συνολική ευεξία.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#14a9ae', halo: 'rgba(225,255,253,.98)', theme: 'light',
    model: 'multivitamin_final.glb', label: 'multivitamin-label.png', type: 'bottle', flipY: true, radius: 1.018, labelAspect: 142 / 53, yStart: .07, seam: Math.PI / 2,
    effects: [
      'home-assets/floaters/multivitamin/multivitamin-tablet-angle-01-front-three-quarter.png',
      'home-assets/floaters/multivitamin/multivitamin-tablet-angle-02-edge-profile.png',
      'home-assets/floaters/multivitamin/multivitamin-tablet-angle-03-near-top.png'
    ]
  },
  {
    id: 'd3k2', name: 'D3 + K2', series: 'CLINICAL SERIES',
    eyebrow: 'ΜΙΚΡΗ ΚΙΝΗΣΗ · ΚΑΘΕ ΜΕΡΑ', title: 'ΗΛΙΑΚΗ ΕΝΕΡΓΕΙΑ.<br>ΣΤΟΧΕΥΜΕΝΑ.',
    description: 'Μια απλή καθημερινή κίνηση, σχεδιασμένη για σταθερή συνέπεια.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#e36d33', halo: 'rgba(255,247,221,.98)', theme: 'light',
    model: 'd3-k2.glb', label: 'd3-k2-label.png', type: 'spray', flipY: false, front: 0,
    effects: ['home-assets/floaters/effects/d3k2-droplets.png']
  },
  {
    id: 'back2balance', name: 'BACK2BALANCE', series: 'CLINICAL SERIES',
    eyebrow: 'ΒΡΕΙΤΕ ΞΑΝΑ ΤΟΝ ΡΥΘΜΟ ΣΑΣ', title: 'ΙΣΟΡΡΟΠΙΑ,<br>ΣΕ ΚΙΝΗΣΗ.',
    description: 'Η σύγχρονη καθημερινότητα αλλάζει ρυθμό. Η υποστήριξή σας ακολουθεί.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#2d65a4', halo: 'rgba(227,245,255,.96)', theme: 'light',
    model: 'back2balance.glb', label: 'back2balance-label.png', type: 'balance', front: 0
  },
  {
    id: 'back2sleep', name: 'BACK2SLEEP', series: 'CLINICAL SERIES',
    eyebrow: 'Η ΝΥΧΤΑ ΞΕΚΙΝΑ ΑΛΛΙΩΣ', title: 'ΚΛΕΙΣΤΕ ΤΗ ΜΕΡΑ.<br>ΗΡΕΜΑ.',
    description: 'Μια νέα προσέγγιση στη βραδινή ρουτίνα, πριν από την επόμενη απαιτητική ημέρα.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#a88ee8', halo: 'rgba(244,231,255,.92)', theme: 'dark',
    model: 'back2sleep.glb', label: 'back2sleep-label.png', type: 'spray', flipY: false, front: 0,
    effects: ['home-assets/floaters/effects/d3k2-droplets.png'], effectClass: 'sleep'
  },
  {
    id: 'back2move', name: 'BACK2MOVE', series: 'CLINICAL SERIES',
    eyebrow: 'ΣΧΕΔΙΑΣΜΕΝΟ ΓΙΑ ΝΑ ΣΥΝΕΧΙΖΕΤΕ', title: 'ΚΙΝΗΣΗ ΧΩΡΙΣ<br>ΠΕΡΙΤΤΑ ΟΡΙΑ.',
    description: 'Καθημερινή φροντίδα που ακολουθεί τον δικό σας ρυθμό κίνησης.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#31a9ae', halo: 'rgba(255,255,255,.96)', theme: 'light',
    model: 'back2move.glb', label: 'back2move-label.png', type: 'move', front: 0
  },
  {
    id: 'back2relief', name: 'BACK2RELIEF', series: 'CLINICAL SERIES',
    eyebrow: 'ΣΤΟΧΕΥΜΕΝΗ ΚΑΘΗΜΕΡΙΝΗ ΦΡΟΝΤΙΔΑ', title: 'ΑΝΑΚΟΥΦΙΣΗ,<br>ΟΤΑΝ ΤΗ ΧΡΕΙΑΖΕΣΤΕ.',
    description: 'Ένας νέος τρόπος να εντάξετε τη στοχευμένη φροντίδα στην καθημερινότητά σας.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#a8273e', halo: 'rgba(255,238,231,.96)', theme: 'light',
    model: 'back2relief.glb', label: 'back2relief-label.png', type: 'relief', front: 0
  },
  {
    id: 'creatine', name: 'CREATINE', series: 'PERFORMANCE SERIES',
    eyebrow: '100% CREATINE MONOHYDRATE', title: 'ΚΑΘΑΡΗ ΔΥΝΑΜΗ.<br>ΜΕΤΡΗΣΙΜΗ ΠΡΟΟΔΟΣ.',
    description: 'Premium ποιότητα, ξεκάθαρος στόχος και συνέπεια σε κάθε προπόνηση.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#08cfe6', halo: 'rgba(224,253,255,1)', theme: 'light', strongHalo: true,
    model: 'creatine-300g.glb', type: 'creatine', front: 0, effects: ['home-assets/floaters/effects/creatine-scoop.png']
  },
  {
    id: 'whey-vanilla', name: 'WHEY · VANILLA', series: 'PERFORMANCE SERIES',
    eyebrow: '100% PURE WHEY PROTEIN', title: 'ΑΠΟΔΟΣΗ ΠΟΥ<br>ΓΙΝΕΤΑΙ ΣΥΝΗΘΕΙΑ.',
    description: 'Premium πρωτεΐνη με καθαρή γεύση βανίλιας, σχεδιασμένη για την καθημερινή σας πρόοδο.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#c6a56a', halo: 'rgba(255,249,222,1)', theme: 'dark', strongHalo: true,
    model: 'whey-2kg.glb', label: 'whey-vanilla-label.png', type: 'whey', front: 0, effects: ['home-assets/floaters/effects/whey-vanilla-scoop.png']
  },
  {
    id: 'whey-chocolate', name: 'WHEY · CHOCOLATE', series: 'PERFORMANCE SERIES',
    eyebrow: '100% PURE WHEY PROTEIN', title: 'Η ΑΠΟΔΟΣΗ ΓΙΝΕΤΑΙ<br>ΑΠΟΛΑΥΣΤΙΚΗ.',
    description: 'Premium πρωτεΐνη με γεύση σοκολάτας, για μια ρουτίνα που θέλετε να επαναλάβετε.',
    cta: 'ΔΕΙΤΕ ΤΟ ΠΡΟΪΟΝ', url: 'https://b2h.gr/', accent: '#b66570', halo: 'rgba(255,226,218,1)', theme: 'dark', strongHalo: true,
    model: 'whey-2kg.glb', label: 'whey-chocolate-label.png', type: 'whey', front: 0, effects: ['home-assets/floaters/effects/whey-chocolate-scoop.png']
  }
];

const $ = (id) => document.getElementById(id);
const canvas = $('product-canvas');
const showcase = $('showcase');
const backgroundsEl = $('backgrounds');
const effectsEl = $('effects');
const haloEl = $('product-halo');
const shadowEl = $('product-shadow');
const copyEl = $('copy');

const clamp = (v, min = 0, max = 1) => Math.min(max, Math.max(min, v));
const ease = (v) => 1 - Math.pow(1 - clamp(v), 3);

products.forEach((p, index) => {
  const bg = document.createElement('div');
  bg.className = 'background-layer';
  bg.dataset.desktop = `home-assets/backgrounds/${p.id}-desktop.png`;
  bg.dataset.mobile = `home-assets/backgrounds/${p.id}-mobile.png`;
  bg.dataset.index = index;
  backgroundsEl.append(bg);

  const effectSet = document.createElement('div');
  effectSet.className = `effect-set ${p.effectClass || ''}`;
  effectSet.dataset.index = index;
  (p.effects || []).forEach((src, i) => {
    const img = document.createElement('img');
    img.dataset.src = src;
    img.alt = '';
    if (src.includes('droplets')) img.className = 'fx-droplets';
    else if (src.includes('scoop')) img.className = 'fx-scoop';
    else img.className = ['fx-a', 'fx-b', 'fx-c'][i % 3];
    effectSet.append(img);
  });
  effectsEl.append(effectSet);
});

$('counter-total').textContent = String(products.length).padStart(2, '0');

const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: true, powerPreference: 'high-performance' });
renderer.setPixelRatio(Math.min(devicePixelRatio, 1.8));
renderer.setSize(innerWidth, innerHeight, false);
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = .92;
renderer.setClearColor(0x000000, 0);

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(33, innerWidth / innerHeight, .01, 100);
scene.add(new THREE.HemisphereLight(0xffffff, 0x20242d, 1.25));
const key = new THREE.DirectionalLight(0xfffdf9, 2.25); key.position.set(3.8, 4.8, 5.5); scene.add(key);
const fill = new THREE.DirectionalLight(0xd7edff, .82); fill.position.set(-4.2, 1.6, 3.5); scene.add(fill);
const rim = new THREE.DirectionalLight(0xffe7c4, .98); rim.position.set(2.2, 1.0, -4.7); scene.add(rim);

const draco = new DRACOLoader();
draco.setDecoderPath('https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/libs/draco/');
const gltfLoader = new GLTFLoader();
gltfLoader.setDRACOLoader(draco);
const textureLoader = new THREE.TextureLoader();

const tuneImportedModel = (model) => {
  const maxAnisotropy = Math.min(16, renderer.capabilities.getMaxAnisotropy());
  model.traverse(node => {
    if (!node.isMesh || !node.material) return;
    const materials = Array.isArray(node.material) ? node.material : [node.material];
    materials.forEach(material => {
      ['map', 'emissiveMap', 'normalMap', 'roughnessMap', 'metalnessMap', 'aoMap'].forEach(key => {
        const map = material[key];
        if (!map) return;
        map.anisotropy = maxAnisotropy;
        if (key === 'map' || key === 'emissiveMap') map.colorSpace = THREE.SRGBColorSpace;
        map.needsUpdate = true;
      });
      if (/Exact_Creatine|Packaging/i.test(material.name)) {
        material.roughness = Math.max(material.roughness ?? 0, .5);
        material.metalness = 0;
        material.envMapIntensity = .58;
      } else if (/Unprinted_Matte_Black/i.test(material.name)) {
        material.roughness = Math.max(material.roughness ?? 0, .48);
        material.envMapIntensity = .5;
      }
      material.needsUpdate = true;
    });
  });
  return model;
};
const loadModel = (url) => new Promise((resolve, reject) => gltfLoader.load(assetUrl(url), g => resolve(tuneImportedModel(g.scene)), undefined, reject));
const loadTexture = async (url, flipY = true, rotation = 0) => {
  const texture = await textureLoader.loadAsync(assetUrl(url));
  texture.colorSpace = THREE.SRGBColorSpace;
  texture.wrapS = THREE.ClampToEdgeWrapping;
  texture.wrapT = THREE.ClampToEdgeWrapping;
  texture.flipY = flipY;
  texture.center.set(.5, .5);
  texture.rotation = rotation;
  texture.anisotropy = Math.min(16, renderer.capabilities.getMaxAnisotropy());
  return texture;
};

const whiteMaterial = () => new THREE.MeshStandardMaterial({ color: 0xeae9e5, roughness: .5, metalness: 0 });
const centerObject = (object) => {
  const box = new THREE.Box3().setFromObject(object);
  object.position.sub(box.getCenter(new THREE.Vector3()));
  return new THREE.Box3().setFromObject(object);
};

async function buildBottle(p) {
  const model = await loadModel(p.model);
  model.traverse(n => { if (n.isMesh) n.material = whiteMaterial(); });
  const wb = centerObject(model);
  const size = wb.getSize(new THREE.Vector3());
  const tex = await loadTexture(p.label, p.flipY);
  const radius = Math.max(size.x, size.z) / 2 * p.radius;
  const labelHeight = Math.PI * 2 * radius / p.labelAspect;
  const geometry = new THREE.CylinderGeometry(radius, radius, labelHeight, 160, 1, true);
  const material = new THREE.MeshStandardMaterial({ map: tex, transparent: true, alphaTest: .015, roughness: .5, side: THREE.FrontSide });
  const label = new THREE.Mesh(geometry, material);
  label.position.y = wb.min.y + size.y * p.yStart + labelHeight / 2;
  label.rotation.y = p.seam;
  const root = new THREE.Group(); root.add(model, label);
  return root;
}

async function buildSpray(p) {
  const model = await loadModel(p.model);
  model.scale.set(1.05, 1, 1.05);
  model.traverse(n => { if (n.isMesh) n.material = whiteMaterial(); });
  const wb = centerObject(model);
  const size = wb.getSize(new THREE.Vector3());
  const tex = await loadTexture(p.label, false, Math.PI);
  const radius = Math.max(size.x, size.z) / 2 * 1.003;
  const labelHeight = Math.PI * 2 * radius / (782 / 326);
  const label = new THREE.Mesh(
    new THREE.CylinderGeometry(radius, radius, labelHeight, 160, 1, true),
    new THREE.MeshStandardMaterial({ map: tex, transparent: true, alphaTest: .015, roughness: .5, side: THREE.FrontSide })
  );
  label.position.y = wb.min.y + size.y * .035 + labelHeight / 2;
  label.rotation.y = Math.PI / 2 - 1.37;
  label.scale.z = -1;
  const root = new THREE.Group(); root.add(model, label);
  return root;
}

async function buildBalance(p) {
  const model = await loadModel(p.model);
  model.traverse(n => { if (n.isMesh) n.material = whiteMaterial(); });
  const wb = centerObject(model);
  const size = wb.getSize(new THREE.Vector3());
  const tex = await loadTexture(p.label, false, Math.PI);
  const yMin = wb.min.y + size.y * .095;
  const yMax = wb.min.y + size.y * .625;
  const labelHeight = yMax - yMin;
  const radius = Math.max(size.x, size.z) / 2 * .9998;
  const label = new THREE.Mesh(
    new THREE.CylinderGeometry(radius, radius, labelHeight, 160, 1, true),
    new THREE.MeshStandardMaterial({ map: tex, transparent: true, alphaTest: .015, roughness: .5, side: THREE.FrontSide })
  );
  label.position.y = (yMin + yMax) / 2;
  label.rotation.y = Math.PI / 2;
  label.scale.z = -1;
  const root = new THREE.Group(); root.add(model, label); root.rotation.y = -Math.PI * .5;
  return root;
}

async function buildMove(p) {
  const model = await loadModel(p.model);
  model.traverse(n => {
    if (!n.isMesh || !n.material) return;
    n.material = n.material.clone();
    if (n.material.name.includes('MatteWhite')) { n.material.color.set(0xf2f1ee); n.material.roughness = .46; n.material.metalness = 0; }
    if (n.material.name.includes('BrushedSilver')) { n.material.color.set(0xaeb2b7); n.material.roughness = .25; n.material.metalness = .92; }
  });
  const wb = centerObject(model);
  const size = wb.getSize(new THREE.Vector3());
  const tex = await loadTexture(p.label, false, Math.PI);
  const rx = size.x * .515, rz = size.z * .515;
  const h = Math.pow((rx - rz) / (rx + rz), 2);
  const circumference = Math.PI * (rx + rz) * (1 + (3 * h) / (10 + Math.sqrt(4 - 3 * h)));
  const labelHeight = circumference / (163 / 58);
  const label = new THREE.Mesh(
    new THREE.CylinderGeometry(1, 1, labelHeight, 160, 1, true),
    new THREE.MeshStandardMaterial({ map: tex, transparent: true, alphaTest: .015, roughness: .5, side: THREE.FrontSide })
  );
  label.scale.set(rx, 1, -rz);
  label.position.y = wb.min.y + size.y * .095 + labelHeight / 2;
  const root = new THREE.Group(); root.add(model, label);
  return root;
}

async function buildRelief(p) {
  const model = await loadModel(p.model);
  model.scale.set(.94, 1.20, .94);
  model.traverse(n => { if (n.isMesh) n.material = whiteMaterial(); });
  const wb = centerObject(model);
  const size = wb.getSize(new THREE.Vector3());
  const tex = await loadTexture(p.label, false, Math.PI);
  const radius = Math.min(size.x, size.z) / 2 * 1.006;
  const labelHeight = Math.PI * 2 * radius / (1726 / 1349);
  const label = new THREE.Mesh(
    new THREE.CylinderGeometry(radius, radius, labelHeight, 160, 1, true),
    new THREE.MeshStandardMaterial({ map: tex, transparent: true, alphaTest: .015, roughness: .5, side: THREE.FrontSide })
  );
  label.position.y = wb.min.y + size.y * .035 + labelHeight / 2;
  label.rotation.y = Math.PI / 2 - 1.28;
  label.scale.z = -1;
  const root = new THREE.Group(); root.add(model, label);
  return root;
}

async function buildWhey(p) {
  const model = await loadModel(p.model);
  model.traverse(n => {
    if (!n.isMesh) return;
    n.material = new THREE.MeshPhysicalMaterial({ color: 0x08090b, roughness: .42, metalness: 0, clearcoat: .24, clearcoatRoughness: .32 });
  });
  const wb = centerObject(model);
  const size = wb.getSize(new THREE.Vector3());
  const tex = await loadTexture(p.label, true);
  const radius = Math.max(size.x, size.z) * .505;
  const labelHeight = Math.PI * 2 * radius / (4096 / 1164);
  const label = new THREE.Mesh(
    new THREE.CylinderGeometry(radius, radius, labelHeight, 160, 1, true),
    new THREE.MeshPhysicalMaterial({ map: tex, transparent: true, alphaTest: .015, roughness: .5, clearcoat: .08, side: THREE.FrontSide })
  );
  label.position.y = wb.min.y + size.y * .105 + labelHeight / 2;
  label.rotation.y = Math.PI;
  const root = new THREE.Group(); root.add(model, label);
  return root;
}

async function buildProduct(p) {
  let root;
  if (p.type === 'bottle') root = await buildBottle(p);
  else if (p.type === 'spray') root = await buildSpray(p);
  else if (p.type === 'balance') root = await buildBalance(p);
  else if (p.type === 'move') root = await buildMove(p);
  else if (p.type === 'relief') root = await buildRelief(p);
  else if (p.type === 'whey') root = await buildWhey(p);
  else root = await loadModel(p.model);

  const box = new THREE.Box3().setFromObject(root);
  root.position.sub(box.getCenter(new THREE.Vector3()));
  const normalizedBox = new THREE.Box3().setFromObject(root);
  const size = normalizedBox.getSize(new THREE.Vector3());
  const outer = new THREE.Group();
  outer.add(root);
  outer.scale.setScalar(2.1 / Math.max(.001, size.y));
  outer.visible = false;
  outer.userData.baseScale = outer.scale.x;
  scene.add(outer);
  return outer;
}

const productGroups = products.map(() => {
  const placeholder = new THREE.Group();
  placeholder.visible = false;
  placeholder.userData.baseScale = 1;
  scene.add(placeholder);
  return placeholder;
});
const productPromises = new Array(products.length);

function ensureProduct(index) {
  if (index < 0 || index >= products.length) return Promise.resolve();
  if (productPromises[index]) return productPromises[index];
  productPromises[index] = buildProduct(products[index]).then(group => {
    scene.remove(productGroups[index]);
    productGroups[index] = group;
    return group;
  }).catch(error => {
    console.error(`Failed to load ${products[index].id}`, error);
    return productGroups[index];
  });
  return productPromises[index];
}

function ensureBackground(index) {
  if (index < 0 || index >= products.length) return;
  const layer = backgroundsEl.children[index];
  if (layer.dataset.ready) return;
  layer.style.backgroundImage = `url("${assetUrl(layer.dataset.desktop)}")`;
  layer.style.setProperty('--mobile-bg', `url("${assetUrl(layer.dataset.mobile)}")`);
  layer.dataset.ready = 'true';
  effectsEl.children[index].querySelectorAll('img[data-src]').forEach(img => {
    img.src = assetUrl(img.dataset.src);
    delete img.dataset.src;
  });
}

let segmentPx = 0;
let targetScroll = 0;
let smoothScroll = 0;
let activeCopy = -1;

function layout() {
  const mobile = innerWidth <= 820;
  segmentPx = innerHeight * (mobile ? 1.32 : 1.28);
  showcase.style.height = `${segmentPx * products.length + innerHeight}px`;
  renderer.setPixelRatio(Math.min(devicePixelRatio, mobile ? 1.45 : 1.8));
  renderer.setSize(innerWidth, innerHeight, false);
  camera.aspect = innerWidth / innerHeight;
  camera.position.set(0, mobile ? .32 : .04, mobile ? 11.8 : 6.05);
  camera.updateProjectionMatrix();
  targetScroll = clamp(scrollY - showcase.offsetTop, 0, segmentPx * products.length);
}

function setCopy(index) {
  if (index === activeCopy) return;
  activeCopy = index;
  const p = products[index];
  $('eyebrow').textContent = p.eyebrow;
  $('title').innerHTML = p.title;
  $('description').textContent = p.description;
  $('cta').querySelector('span').textContent = p.cta;
  $('cta').href = p.url;
  $('caption-name').textContent = p.name;
  $('caption-series').textContent = p.series;
  $('counter-current').textContent = String(index + 1).padStart(2, '0');
  document.documentElement.style.setProperty('--accent', p.accent);
  document.documentElement.style.setProperty('--halo', p.halo);
  document.body.classList.toggle('theme-dark', p.theme === 'dark');
  haloEl.classList.toggle('strong', Boolean(p.strongHalo));
}

function updateStage(scrollPosition) {
  const max = segmentPx * products.length;
  const clamped = clamp(scrollPosition, 0, max - .001);
  const index = Math.min(products.length - 1, Math.floor(clamped / segmentPx));
  const local = clamp((clamped - index * segmentPx) / segmentPx);
  const hasNext = index < products.length - 1;
  const transition = hasNext ? ease((local - .72) / .28) : 0;
  const spin = clamp(local / .72);
  const copyIndex = transition > .5 && hasNext ? index + 1 : index;
  ensureBackground(index);
  ensureBackground(index + 1);
  ensureProduct(index);
  ensureProduct(index + 1);
  ensureProduct(index + 2);
  setCopy(copyIndex);

  const copyFade = hasNext && local > .72 ? clamp(Math.abs(transition * 2 - 1), .06, 1) : 1;
  copyEl.style.opacity = copyFade;
  const copyShift = transition <= .5 ? -transition * 22 : (1 - transition) * 22;
  copyEl.style.transform = innerWidth <= 820 ? `translate3d(${copyShift}px,0,0)` : `translate3d(${copyShift}px,-50%,0)`;

  productGroups.forEach(g => { g.visible = false; });
  const current = productGroups[index];
  const mobile = innerWidth <= 820;
  const currentBaseX = mobile ? 0 : (products[index].desktopX ?? .82);
  current.visible = true;
  current.rotation.y = (products[index].front ?? Math.PI / 2) + spin * Math.PI * 2 + transition * Math.PI * 1.15;
  current.rotation.z = -transition * .42;
  current.position.set(currentBaseX - transition * 4.6, mobile ? 1.35 : .06, 0);
  const currentScale = current.userData.baseScale || 1;
  current.scale.setScalar(currentScale * (1 - transition * .16));

  if (hasNext && transition > .001) {
    const next = productGroups[index + 1];
    const nextBaseX = mobile ? 0 : (products[index + 1].desktopX ?? .82);
    next.visible = true;
    next.position.set(nextBaseX + (1 - transition) * 4.6, mobile ? 1.35 : .06, 0);
    next.rotation.y = (products[index + 1].front ?? Math.PI / 2) - (1 - transition) * Math.PI * 1.15;
    next.rotation.z = (1 - transition) * .42;
    const nextScale = next.userData.baseScale || 1;
    next.scale.setScalar(nextScale * (.84 + transition * .16));
  }

  [...backgroundsEl.children].forEach((layer, i) => {
    let opacity = 0, x = 12;
    if (i === index) { opacity = 1 - transition; x = -transition * 14; }
    if (hasNext && i === index + 1) { opacity = transition; x = (1 - transition) * 14; }
    layer.style.opacity = opacity;
    layer.style.transform = `translate3d(${x}%,0,0) scale(1.04)`;
  });
  [...effectsEl.children].forEach((layer, i) => {
    let opacity = 0, x = 0, y = 0, rot = 0;
    if (i === index) { opacity = 1 - transition; x = -transition * 34; y = -spin * 12; rot = spin * 22; }
    if (hasNext && i === index + 1) { opacity = transition; x = (1 - transition) * 34; y = (1 - transition) * 12; rot = -(1 - transition) * 22; }
    layer.style.opacity = opacity;
    layer.style.transform = `translate3d(${x}vw,${y}px,0) rotate(${rot}deg)`;
  });

  const desktopVisualOffset = mobile ? 0 : 11;
  haloEl.style.transform = `translate(calc(-50% + ${desktopVisualOffset - transition * 4.6}vw),-50%) scale(${1 + Math.sin(spin * Math.PI) * .07})`;
  haloEl.style.opacity = products[copyIndex].strongHalo ? .98 : .78;
  shadowEl.style.transform = `translateX(calc(-50% + ${desktopVisualOffset - transition * 4.6}vw)) scaleX(${1 - transition * .22})`;
  $('scroll-progress').style.transform = `scaleX(${clamp(scrollPosition / max)})`;
}

addEventListener('scroll', () => {
  targetScroll = clamp(scrollY - showcase.offsetTop, 0, segmentPx * products.length);
}, { passive: true });
addEventListener('resize', layout);

ensureBackground(0);
ensureBackground(1);
ensureProduct(0);
ensureProduct(1);
layout();
setCopy(0);
updateStage(0);

function animate() {
  requestAnimationFrame(animate);
  smoothScroll = targetScroll;
  updateStage(smoothScroll);
  renderer.render(scene, camera);
}
animate();
