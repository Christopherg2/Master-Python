<!DOCTYPE html>
<html lang="en">
  <head>
    <script src="https://cdn.jsdelivr.net/npm/mind-ar@1.1.4/dist/mindar-image.prod.js"></script>
    <script src="https://aframe.io/releases/1.2.0/aframe.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/mind-ar@1.1.4/dist/mindar-image-aframe.prod.js"></script>
    <title>RA GIT HUB</title>
  </head>
  <body>
    <a-scene
      mindar-image="imageTargetSrc:https://cdn.glitch.global/9eecc002-eb91-4374-84e9-7bd19775bc6e/targets.mind?v=1648048229138;"
      vr-mode-ui="enabled: false"
      device-orientation-permission-ui="enabled: false"
    >
      <a-camera position="0 0 0" look-controls="enabled: false"></a-camera>
      <a-entity mindar-image-target="targetIndex: 0">
        <a-gltf-model
          rotation="0 0 0"
          position="0 0 0.1"
          scale="0.5 0.5 0.5"
          src="https://cdn.glitch.global/9eecc002-eb91-4374-84e9-7bd19775bc6e/EEEEEEEEEE.glb?v=1648049833594"
        ></a-gltf-model>
      </a-entity>
    </a-scene>
  </body>
</html>
