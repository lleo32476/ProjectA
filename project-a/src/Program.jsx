import { useState } from "react";

function Program({address}){
    //variables
    const [item, setItem] = useState("");
    const [itemList, setItemList] = useState([]);

    //function to read textboxes on the website through ID
    function readTextbox(id) {
        const textbox = document.getElementById(id); 
        const textValue = textbox.value; console.log(textValue); 
    return textValue }
    
    async function store_finder(lookup_item){
        const response = await fetch("http://localhost:5000/StoreFinder", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                address: address,
                lookup_item: lookup_item,
            })
        });
        const data = await response.json(); // parse Flask's list
        return data;
    }

    return(
        <>
            <input
                type="text"
                id="search_bar"
                placeholder="Search"
                onKeyDown={async (e) => {
                    if (e.key === 'Enter') {
                        const lookup_item = readTextbox("search_bar");
                        setItem(lookup_item)
                        const list = await store_finder(lookup_item)
                        setItemList(list)
                    }
                }}
            ></input>
            <button 
                onClick = {async () => {
                    const lookup_item = readTextbox("search_bar")
                    setItem(lookup_item)
                    const list = await store_finder(lookup_item)
                    setItemList(list)
                }}>
                Search
                </button>
            <ul>{itemList.map((x, i) => <li key={i}>{x.name} - ${x.price} ({x.size})</li>)}</ul>
        </>
    );
}

export default Program