function DisplayArea({ displayItems }) {
    if (!displayItems || displayItems.length === 0) return <p>No results yet.</p>;
    return (
        <ul>
            {displayItems.map((x, i) => (
                <li key={i}>{x.name} - ${x.price} ({x.size}) {x.store}</li>
            ))}
        </ul>
    );
}

export default DisplayArea