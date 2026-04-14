import { useEffect, useState } from "react";
import { getTasks, createTask } from "../api/task";

export default function Home() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    getTasks().then(setTasks);
  }, []);

  return (
    <div>
      <h1>Task List</h1>

      <ul>
        {tasks.map((t: any) => (
          <li key={t.id}>{t.title}</li>
        ))}
      </ul>
    </div>
  );
}
