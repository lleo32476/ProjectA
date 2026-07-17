import Header from './Header.jsx';
import Footer from './Footer.jsx';
import InputAddress from './InputAddress.jsx';
import { useState } from "react";
import Program from './Program.jsx';

function App() {
    //variables
    const [fullAddress, setFullAddress] = useState("");

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
    setFullAddress(text)
    console.log(fullAddress)
    }

    if (fullAddress === "") {
        return(
            <>
                <Header></Header>
                <InputAddress></InputAddress>
                <button onClick={get_address}>Read Button Test</button>
                <Footer></Footer>
            </>
        )
    }

    return(
      <>
          <Header></Header>
          <Program address = {fullAddress}></Program>
          <h1>{fullAddress}</h1>
          <Footer></Footer>
      </>
    );
}

export default App
