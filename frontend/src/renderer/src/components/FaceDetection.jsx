import React from "react"

export default function Facedetection() {
  return (
    <div className="h-full w-full bg-gray-700 bg-opacity-75 absolute left-0 top-0 flex items-center justify-center">
      <div className="bg-neutral-500 rounded-md border-neutral-700 border-4 bg-opacity-85 p-3 flex flex-col items-center gap-3 w-[60rem] h-[30rem]">
        <p className="flex justify-center font-bold text-lg">Aproxime o rosto da câmera</p>
        <video src=""></video>
      </div>
    </div>
  )
}
