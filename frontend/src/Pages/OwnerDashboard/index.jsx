import React, { useState } from 'react';
import PetManagement from './components/PetManagement';
import ServiceBooking from './components/ServiceBooking';
import OwnerProfile from './components/OwnerProfile';
import './OwnerDashboard.css';

export default function OwnerDashboard() {
  const [activeTab, setActiveTab] = useState('profile');

  return (
    <div className="owner-dashboard">
      <aside className="owner-sidebar">
        <div className="sidebar-header">
          <h2>Propietario</h2>
        </div>
        <nav className="sidebar-nav">
          <button
            className={`nav-btn ${activeTab === 'profile' ? 'active' : ''}`}
            onClick={() => setActiveTab('profile')}
          >
            Mi Perfil
          </button>
          <button
            className={`nav-btn ${activeTab === 'pets' ? 'active' : ''}`}
            onClick={() => setActiveTab('pets')}
          >
            Mis Mascotas
          </button>
          <button
            className={`nav-btn ${activeTab === 'booking' ? 'active' : ''}`}
            onClick={() => setActiveTab('booking')}
          >
            Agendar Servicios
          </button>
        </nav>
      </aside>

      <main className="owner-main">
        {activeTab === 'profile' && <OwnerProfile />}
        {activeTab === 'pets' && <PetManagement />}
        {activeTab === 'booking' && <ServiceBooking />}
      </main>
    </div>
  );
}