import React, { useState } from "react";
import Fingerprint from "./components/fingerprint";
import Facedetection from "./components/FaceDetection";

export default function App(){

  const [showAuthentication, setShowAuthentication] = useState(false) //false

  function handleClick(){
    setShowAuthentication(!showAuthentication)
  }

  return(
    <div className="h-full w-full flex justify-center items-center">
      <div className="w-80 bg-neutral-500 rounded-md border-neutral-700 border-4 bg-opacity-85 p-3 flex flex-col items-center gap-3">
        <div className="px-5 py-1 max-w-fit bg-neutral-700 rounded-md text-white">LOGIN</div>
        <div className="flex flex-col gap-2 w-full">
          <input className="rounded-md pl-1 h-7 focus:outline-none" placeholder="Username" type="text" />
          <input className="rounded-md pl-1 h-7 focus:outline-none" placeholder="Password" type="password" />
        </div>
        <button onClick={handleClick} className="bg-green-900 hover:bg-green-700 text-white rounded-xl py-2 px-4">Login</button>
      </div>
      {showAuthentication && <Fingerprint handleModalVisibility={handleClick} />}
      {/* {showAuthentication && <Facedetection />} */}
    </div>
  )
}