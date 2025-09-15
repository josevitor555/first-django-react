
import { useEffect, useState } from 'react';

import './App.css'

const App = () => {

  // Define interface for the data structure
  interface Post {
    id: number;
    title: string;
    body: string;
  }

  // States
  const [data, setData] = useState<Post[]>([]);

  useEffect(() => {
    async function fetchData() {
      console.log(import.meta.env.VITE_API_URL);
      try {
  
        const response = await fetch(`${import.meta.env.VITE_API_URL}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }

        const result = await response.json();
        console.log(result);
        setData(result);

      } catch (error) {
        console.log(error);
      }
    }

    // Call function
    fetchData();
  }, []);

  return (
    <div className="app">
      <h1> Hello World! </h1>
    </div>
  );
}

export default App;
