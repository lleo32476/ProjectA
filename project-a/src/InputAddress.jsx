import { useState } from "react";

function InputAddress({onAddress}){

    //function to read textboxes on the website through ID
    function readTextbox(id) {
        const textbox = document.getElementById(id); 
        const textValue = textbox.value; console.log(textValue); 
    return textValue }

    //function that calls flask to run a python function to read and combine my address together
    async function get_address() {
        var street_address = readTextbox("street_address");
        var city = readTextbox("city");
        var state = readTextbox("state");
        var zip_code = readTextbox("zip_code");

        const response = await fetch("http://localhost:5000/get_address", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                street_address: street_address,
                city: city,
                state: state,
                zip_code: zip_code
            })
        });

    const text = await response.text();
    onAddress(text);
    }



    return(
        <>
            <input 
                type="text" 
                id="street_address" 
                placeholder="Street Address"
            ></input>
            <input 
                type="text" 
                id="city" 
                placeholder="City"
            ></input>
            <input 
                type="text" 
                id="state" 
                placeholder="State"
            ></input>
            <input 
                type="text" 
                id="zip_code" 
                placeholder="Zip Code"
            ></input>
            <button onClick={get_address}>Enter Address</button>
        </>
    );
}

export default InputAddress