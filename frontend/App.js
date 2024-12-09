import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

function App() {
    const [resources, setResources] = useState([]);

    useEffect(() => {
        axios.get('http://localhost:5000/resources')
            .then(response => setResources(response.data))
            .catch(err => console.error(err));
    }, []);

    return (
        <div className="App">
            <h1>Campus Resource Finder</h1>
            <MapContainer center={[51.505, -0.09]} zoom={13} style={{ height: '80vh', width: '100%' }}>
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                />
                {resources.map(resource => (
                    <Marker key={resource.id} position={[resource.latitude, resource.longitude]}>
                        <Popup>
                            <strong>{resource.name}</strong>
                            <p>{resource.category}</p>
                        </Popup>
                    </Marker>
                ))}
            </MapContainer>
        </div>
    );
}

export default App;
