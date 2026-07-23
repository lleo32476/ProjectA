import { useState } from "react";

function SearchBar({FullAddress, onResults}){
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
                address: FullAddress,
                lookup_item: lookup_item,
            })
        });
        const data = await response.json(); // parse Flask's list
        return data;
    }

    const handleSearch = async () => {
        if (!item.trim()) return;
        const list = await store_finder(item);
        onResults(list);
    }

    return(
        <div className="search-bar">
            <input
                type="text"
                id="search_bar"
                placeholder="Search"
                value = {item}
                onChange={(e) => setItem(e.target.value)}
                onKeyDown={async (e) => {
                    if (e.key === 'Enter') {
                        handleSearch();
                    }
                }}
            ></input>
            <button onClick = {handleSearch}> Search </button>
        </div>
    );
}

export default SearchBar