import React from "react"
import axios from 'axios'
import fingerprit_img from "../assets/fingerprint_img.jpg"
import { useNavigate } from "react-router-dom";

export default function Fingerprint({handleModalVisibility, showFacialModal}) {
  const navigate = useNavigate(); // Hook para navegação

  async function handleFinger(type) {
    const data = {
      'type': type
    };

    axios.post('http://localhost:8000/server/fingerprint', data)
    .then(
      (response) => {
        if (response.data.access_level == 3 && response.data.score >= 90.0){
          console.log(response.data)
          showFacialModal()
        }
        else if (response.data.access_level != 3 && response.data.score >= 90.0){
          console.log(response.data)
          navigate('/home')
        }
        else if (response.data.score < 90.0){
          console.log("Digital incorreta!")
        }
      }
    )
    .catch(
      (error) => {
        console.log('Erro ao fazer a autenticação!')
      }
    )
  }

  return (
    <div className="h-full w-full bg-gray-700 bg-opacity-75 absolute left-0 top-0 flex items-center justify-center">
      <div className="bg-neutral-500 rounded-md border-neutral-700 border-4 bg-opacity-85 p-3 flex flex-col items-center gap-3 w-80">
        <div className="bg-white border-2 border-neutral-700 rounded-lg overflow-hidden">
          <img src={fingerprit_img} alt="" />
          <p className="flex justify-center font-semibold text-lg">Aproxime o dedo do sensor</p>
        </div>
        <div className="flex gap-4">
          <button onClick={()=>{handleFinger('wrong')}} className="bg-orange-700 hover:bg-orange-600 text-black font-semibold px-4 py-2 rounded-lg">Dedo errado</button>
          <button onClick={()=>{handleFinger('correct')}} className="bg-green-900 hover:bg-green-700 text-black font-semibold px-4 py-2 rounded-lg">Dedo Correto</button>
        </div>
        <button className="bg-red-500 hover:bg-red-400 text-black font-semibold px-4 py-2 rounded-lg" onClick={handleModalVisibility}>Fechar</button>
      </div>
    </div>
  )
}
