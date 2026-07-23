import './Header.css'
import SearchBar from './SearchBar';

function Header({address, onResults}) {
  return (
    <>
      <header>
        <h1>Project A</h1>
        <SearchBar 
          FullAddress = {address}
          onResults = {onResults}
        ></SearchBar>
        <nav>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About</a></li>
            <li><a href="#">Contact</a></li>
          </ul>
        </nav>
      </header>
      <hr />
    </>
  );
}

export default Header