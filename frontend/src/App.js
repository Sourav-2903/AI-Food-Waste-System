import "./App.css";

function App() {
  return (
    <div className="container">

      <h1>🍲 AI Food Waste System</h1>

      <p>
        Reduce food waste through AI-powered
        donation management.
      </p>

      <div className="cards">

        <div className="card">
          <h2>Donor Portal</h2>
          <p>
            Donate excess food
          </p>
        </div>

        <div className="card">
          <h2>NGO Portal</h2>
          <p>
            Request food pickups
          </p>
        </div>

        <div className="card">
          <h2>Admin Dashboard</h2>
          <p>
            Monitor system activity
          </p>
        </div>

      </div>

    </div>
  );
}

export default App;