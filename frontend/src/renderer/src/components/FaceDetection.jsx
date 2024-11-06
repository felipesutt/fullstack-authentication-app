import React, { useEffect, useRef } from 'react'
import Webcam from 'react-webcam'
import { useNavigate } from "react-router-dom";
import axios from 'axios';

export default function Facedetection() {
  const webcamRef = useRef(null)
  const navigate = useNavigate(); // Hook para navegação

  // Função para enviar a imagem
  async function sendImage(imageSrc){
    try{
      const response = await axios.post('http://localhost:8000/server/facial', {
        image: imageSrc, // Envia a imagem base64
      });
      console.log('Imagem enviada com sucesso!');
      console.log(response.data);
      if (response.data.access_granted === 'True'){
        navigate('/home')
      }
    } catch (error){
      console.error('Erro ao enviar imagem:', error);
    }
  }

  // Função para capturar imagem
  function capture(){
    const imageSrc = webcamRef.current.getScreenshot(); // Captura a imagem
    if (imageSrc){
      sendImage(imageSrc); // Envia a imagem para o backend
    }
    else{
      console.log('Não foi possivel capturar a imagem!')
    }
  }

  // UseEffect para capturar a imagem a cada intervalo de tempo
  useEffect(() => {
    const intervalId = setInterval(() => {
      capture(); // Chama a função de captura a cada intervalo
    }, 2000); // Captura a cada 2 segundos

    return () => clearInterval(intervalId); // Limpa o intervalo ao desmontar o componente
  }, []);

  return (
    <div className="h-full w-full bg-gray-700 bg-opacity-75 absolute left-0 top-0 flex items-center justify-center">
      <div className="bg-neutral-500 rounded-md border-neutral-700 border-4 bg-opacity-85 p-3 flex flex-col items-center gap-3 w-[60rem] h-[30rem]">
        <p className="flex justify-center font-bold text-lg">Aproxime o rosto da câmera</p>
        <Webcam
          audio={false}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={640}
          height={480}
        />
      </div>
    </div>
  )
}
