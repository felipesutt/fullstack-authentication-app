import React, { useEffect, useRef } from 'react'

export default function Facedetection() {
  const videoRef = useRef(null);

  useEffect(() => {
      const startVideo = async () => {
          try {
              // Solicita acesso à câmera
              const stream = await navigator.mediaDevices.getUserMedia({ video: true });
              if (videoRef.current) {
                  videoRef.current.srcObject = stream;
              }
          } catch (error) {
              console.error("Erro ao acessar a câmera: ", error);
          }
      };

      startVideo();

      // Limpeza: Para parar o stream da câmera quando o componente for desmontado
      return () => {
          if (videoRef.current && videoRef.current.srcObject) {
              const tracks = videoRef.current.srcObject.getTracks();
              tracks.forEach(track => track.stop());
          }
      };
  }, []);

  return (
    <div className="h-full w-full bg-gray-700 bg-opacity-75 absolute left-0 top-0 flex items-center justify-center">
      <div className="bg-neutral-500 rounded-md border-neutral-700 border-4 bg-opacity-85 p-3 flex flex-col items-center gap-3 w-[60rem] h-[30rem]">
        <p className="flex justify-center font-bold text-lg">Aproxime o rosto da câmera</p>
        <video ref={videoRef} width="640" height="480" autoPlay></video>
      </div>
    </div>
  )
}
