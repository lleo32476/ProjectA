import Header from './Header.jsx';
import Footer from './Footer.jsx';
import InputAddress from './InputAddress.jsx';
import { useState } from "react";
import DisplayArea from './DisplayArea.jsx';

function App() {
    //variables
    const [fullAddress, setFullAddress] = useState("");
    const [itemsList, setItemsList] = useState([])

    return(
      <>
          <Header address = {fullAddress} onResults = {setItemsList}></Header>
          <InputAddress onAddress = {setFullAddress}></InputAddress>
          <DisplayArea displayItems = {itemsList}></DisplayArea>
          <Footer></Footer>
      </>
    );
}

export default App
