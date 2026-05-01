# Route Optimization System

An interactive web application for route planning and graph analysis using Bellman-Ford and Floyd-Warshall shortest-path algorithms. The app combines route search, graph visualization, analytics, traffic simulation, and city or road management in one Flask-based dashboard.

## Screenshots

Add the screenshot files listed below into [`docs/screenshots`](C:\Users\B NAVANEETH\Route_Optimization_System\docs\screenshots\README.md), and GitHub will render them automatically in this gallery.

### Home Dashboard

![Home Dashboard](docs/screenshots/01-home-dashboard.png)

### Route Finder

![Route Finder](docs/screenshots/02-route-finder.png)

### Graph Visualization

![Graph Visualization](docs/screenshots/03-graph-visualization.png)

### Live Map View

![Live Map View](docs/screenshots/04-live-map-view.png)

### Algorithm Comparison

![Algorithm Comparison](docs/screenshots/05-algorithm-comparison.png)

### Traffic Simulation

![Traffic Simulation](docs/screenshots/06-traffic-simulation.png)

### Manage Cities and Roads

![Manage Cities and Roads](docs/screenshots/07-manage-cities-roads.png)

### Analytics Dashboard

![Analytics Dashboard](docs/screenshots/08-analytics-dashboard.png)

## Features

- Multi-page dashboard for route analysis, graph exploration, and operations
- Bellman-Ford and Floyd-Warshall implementations built from scratch
- Interactive D3.js graph visualization with zoom, pan, drag, and path highlighting
- Route comparison with execution-time insights
- Traffic simulation with dynamic edge-weight updates
- Manage cities and road connections with CRUD-style workflows
- Analytics dashboard for graph metrics and degree distribution
- Leaflet-based live map view for geographic exploration

## Tech Stack

| Layer | Technology |
| --- | --- |
| Frontend | HTML5, CSS3, Vanilla JavaScript, D3.js, Leaflet |
| Backend | Python, Flask, Flask-CORS |
| Data | JSON |
| Algorithms | Bellman-Ford, Floyd-Warshall |

## Quick Start

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
pip install -r backend/requirements.txt
python run.py
```

### Access

Open the app at `http://localhost:5000`.

If port `5000` is already being used on your machine, run the app on another port for screenshot capture or testing.

## Project Structure

```text
Route_Optimization_System/
|-- backend/
|   |-- algorithms/
|   |-- data/
|   |-- models/
|   |-- routes/
|   |-- services/
|   `-- app.py
|-- frontend/
|   |-- src/
|   |   |-- components/
|   |   |-- pages/
|   |   |-- services/
|   |   `-- styles/
|   `-- index.html
|-- docs/
|   `-- screenshots/
|-- run.py
`-- README.md
```

## Main Pages

1. Home Dashboard
2. Route Finder
3. Graph Visualization
4. Live Map View
5. Algorithm Comparison
6. Traffic Simulation
7. Manage Cities and Roads
8. Analytics Dashboard

## API Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | `/api/cities` | List all cities |
| GET | `/api/graph` | Get full graph data |
| POST | `/api/route` | Compute shortest route |
| POST | `/api/city` | Add a city |
| POST | `/api/road` | Add a road |
| PUT | `/api/traffic` | Update traffic multiplier |
| DELETE | `/api/city/{id}` | Delete a city |
| GET | `/api/analytics` | Get graph analytics |
| POST | `/api/compare` | Compare both algorithms |

## Algorithms

### Bellman-Ford

- Time complexity: `O(V * E)`
- Space complexity: `O(V)`
- Best for single-source shortest-path queries

### Floyd-Warshall

- Time complexity: `O(V^3)`
- Space complexity: `O(V^2)`
- Best for all-pairs shortest-path analysis

## Screenshot Notes

- Use `PNG` format for the cleanest README rendering.
- Keep screenshots at a consistent width for a cleaner gallery.
- Capture the app with loaded data, not empty states.
- Prefer light mode unless your project is being presented in dark mode throughout.
- Save all screenshots in [`docs/screenshots`](C:\Users\B NAVANEETH\Route_Optimization_System\docs\screenshots\README.md).

## License

MIT
