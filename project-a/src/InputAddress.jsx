
function InputAddress(){



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
        </>
    );
}

export default InputAddress