import React from "react"
import fingerprit_img from "../assets/fingerprint_img.jpg"

export default function Fingerprint({handleModalVisibility}) {
  return (
    <div className="h-full w-full bg-gray-700 bg-opacity-75 absolute left-0 top-0 flex items-center justify-center">
      <div className="bg-neutral-500 rounded-md border-neutral-700 border-4 bg-opacity-85 p-3 flex flex-col items-center gap-3 w-80">
        <div className="bg-white border-2 border-neutral-700 rounded-lg overflow-hidden">
          <img src={fingerprit_img} alt="" />
          <p className="flex justify-center font-semibold text-lg">Aproxime o dedo do sensor</p>
        </div>
        <div className="flex gap-4">
          <button className="bg-orange-700 hover:bg-orange-600 text-black font-semibold px-4 py-2 rounded-lg">Dedo errado</button>
          <button className="bg-green-900 hover:bg-green-700 text-black font-semibold px-4 py-2 rounded-lg">Dedo Correto</button>
        </div>
        <button className="bg-red-500 hover:bg-red-400 text-black font-semibold px-4 py-2 rounded-lg" onClick={handleModalVisibility}>Fechar</button>
      </div>
    </div>
  )
}
