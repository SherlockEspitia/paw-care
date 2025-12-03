import React, { useState } from 'react';
import DaycareDashboard from './components/DaycareDashboard';
import TrainerDashboard from './components/TrainerDashboard';
import WalkerDashboard from './components/WalkerDashboard';
import CaregiverProfile from './components/CaregiverProfile';
import './CaregiverDashboard.css';

export default function CaregiverDashboard() {
  const [activeTab, setActiveTab] = useState('profile');
  // En un caso real, esto vendría del contexto de autenticación
  const [caregiverType, setCaregiverType] = useState('paseador'); // 'guarderia', 'adiestrador', 'paseador'

  return (
    <div className="caregiver-dashboard">
      <aside className="caregiver-sidebar">
        <div className="sidebar-header">
          <h2>Cuidador</h2>
          <span className={`badge-${caregiverType}`}>{caregiverType}</span>
        </div>
        <nav className="sidebar-nav">
          <button
            className={`nav-btn ${activeTab === 'profile' ? 'active' : ''}`}
            onClick={() => setActiveTab('profile')}
          >
            Mi Perfil
          </button>
          <button
            className={`nav-btn ${activeTab === 'services' ? 'active' : ''}`}
            onClick={() => setActiveTab('services')}
          >
            Mis Servicios
          </button>
          <button
            className={`nav-btn ${activeTab === 'bookings' ? 'active' : ''}`}
            onClick={() => setActiveTab('bookings')}
          >
            Mis Citas
          </button>
          <button
            className={`nav-btn ${activeTab === 'ratings' ? 'active' : ''}`}
            onClick={() => setActiveTab('ratings')}
          >
            Calificaciones
          </button>
        </nav>
      </aside>

      <main className="caregiver-main">
        {activeTab === 'profile' && <CaregiverProfile caregiverType={caregiverType} />}
        {activeTab === 'services' && caregiverType === 'guarderia' && <DaycareDashboard />}
        {activeTab === 'services' && caregiverType === 'adiestrador' && <TrainerDashboard />}
        {activeTab === 'services' && caregiverType === 'paseador' && <WalkerDashboard />}
      </main>
    </div>
  );
}