import React, { useState, useEffect } from "react";
import axios from "axios"

export default function Home(){

    const [propriedades, setPropriedades] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:8000/server/getinfo')
        .then(
        (response) => {
            console.log(response.data)
            setPropriedades(response.data.propriedades)
        }
        )
        .catch(
        (error) => {
            console.log('Erro ao fazer login!')
        }
        )
    }, []);

  return(
    <div className="h-full w-full p-28 flex justify-center items-center">
        <div className="w-full h-full bg-neutral-500 rounded-md border-neutral-700 border-4 bg-opacity-85 p-3 flex flex-col items-center gap-3 overflow-y-scroll">
            {propriedades.map((propriedade, index) => (
                <div className="h-36 w-full border-b-black border-b-2 flex flex-row items-center">
                    <div className="w-full h-36 px-8 flex flex-row justify-between items-center text-white">
                        <p>{propriedade.id}</p>
                        <div>
                            <p>Proprietário: {propriedade.responsavel}</p>
                            <p>Propriedade: {propriedade.propriedade}</p>
                        </div>
                        <div>
                            <p>Descrição: {propriedade.content}</p>
                        </div>
                        <div>
                            <p>Nível de acesso: {propriedade.required_access_level}</p>
                        </div>
                    </div>
                </div>
            ))}

        </div>
    </div>
  )
}