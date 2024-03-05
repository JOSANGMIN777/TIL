프로젝트를 위해 three.js를 사용하기로 했다. 
이를 위해 조사하고 공부한 three.js관련 정보들을 정리해보았다.

### Three.js의 구성요소
Scene, Camera, Renderer 이 세가지로 나뉜다. 

- Scene : 렌더링할 모든 객체와 광원을 저장하는 공간
- Camera : Scene 객체를 어떻게 촬영하여 보여줄 것인가 결정
- Renderer : 핵심 객체로 Scene과 Camera 객체를 넘겨받아 렌더링
```
$ npm install three  // three.js 설치

<canvas id="canvas"></canvas>  // WebGL에서 사용하기위해 canvas 태그 호출(필수)



<script type="importmap">
  {
  	"imports": {
      "three": "https://unpkg.com/three@0.138.3/build/three.module.js",
      "GLTFLoader":
      "https://unpkg.com/three@0.141.0/examples/jsm/loaders/GLTFLoader.js"
    }
  }
</script>

<script type="module">  // 라이브러리 기능 사용을 위해 사용 (위에꺼 써야되는건지 의문)
  import * as THREE from 'three';
</script>
```
```
let scene = new THREE.Scene(); // Scene객체생성(필수)

scene.background = new THREE.Color("red"); // 배경색 선택

OrthographicCamera // 원근법 무시
PerspectiveCamera // 원근법 적용

let camera = new THREE.PerspectiveCamera(
  45,
  window.innerWidth / window.innerHeight,
  0.1,
  1000
)

camera.position.set(0, 0, 5);  // 카메라의 위치 설정 (x: 0, y: 0, z: 5)
```
```
import { GLTFLoader } from "GLTFLoader";

let loader = new GLTFLoader();  // 3D 모델 불러오기

loader.load("duck/scene.gltf", function (gltf) {
  scene.add(gltf.scene);
});
```
```
// THREE.AmbientLight(color, intensity) // 빛의 시작점 없이 물체의 모든 면을 골고루 비추는 빛
빛 색상 : color 빛 강도 : intensity

let light = new THREE.AmbientLight();

light.color = 0xffff00;
light.intensity = 5;


// THREE.HemisphereLight(skyColor, groundColor, intensity); // 하늘과 바닥 두 곳의 광원을 가지는 빛

let light = new THREE.HemisphereLight(0xffff00, 0xff0000, 0.3);


// THREE.DirectionalLight(color, intensity); // 먼거리에서 모든 물체에 같은 각도로 비추는 빛

let light = new THREE.DirectionalLight(0xffff00, 0.7);


// Three.PointLight(color, intensity, distance, decay); // 한 지점에서 모든 방향으로 방출되는 빛 distance : 빛 방출 거리 decay : 거리에 따라 빛이 소실되어 어두워지는 정도

let light = new THREE.PointLight(0xffffff, 0.5, 15, 3);


// THREE.RectAreaLight(color, intensity, width, height); // 사각평면에서 균일하게 방출되는 빛 width : 광원의 가로크기 height : 광원의 세로크기 (둘 다 기본값 10)

let light = new THREE.RectAreaLight(0xffff00, 0.5, 20, 20);


// THREE.SpotLight(color, intensity, distance, angle, penumbra, decay); // 한 지점에서 한 방향으로 원뿔형으로 방출 angle : 빛이 퍼지는 각도(PI/2가 최댓값) penumbra : 빛의 가장자리의 선명도 (기본값0, 숫자가 커질수록 가장자리 흐릿해짐)

let light = new THREE.SpotLight(0x00ff00, 1, 30, Math.PI * 0.2, 0.1, 1);

사용예제
let PLight = new THREE.PointLight();
let ALight = new THREE.AmbientLight();
PLight.position.set(50, 50, 50);
scene.add(PLight, ALight);
```
```
let renderer = new THREE.WebGLRenderer({
  canvas: document.querySelector("#canvas"),
  antialias: true,
});

renderer.outputEncoding = THREE.sRGBEncoding;
renderer.setSize(window.innerWidth, window.innerHeight);
```
WebGLRenderer를 통해 renderer 객체를 생성해준다. 이 때, 생성자 함수는 랜더링한 것들을 보여줄 Canvas 태그를 매개변수로 받는다. 그리고 3D 모델의 테두리를 부드럽게 하기 위해 antialias: true를 추가해준다.
보다 정확한 색상을 랜더링하기 위해 outputEncoding 값을 설정해주었고, setSize 메서드를 활용하여 renderer의 크기를 조절해주었다.
이제 loader 객체의 콜백 함수 내에서 renderer의 render 메서드를 통해 랜더링해준다.
```
loader.load("duck/scene.gltf", function (gltf) {
  scene.add(gltf.scene);
  renderer.render(scene, camera); // 랜더링
});
```

근데 코드가 이게 맞냐..?? r3f 도 한번 알아봐야겠다.