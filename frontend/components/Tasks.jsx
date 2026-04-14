import { useEffect, useState } from "react";

export default function Tasks() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    fetch("https://task-app-core2.onrender.com/tasks")
      .then(res => res.json())
      .then(data => setTasks(data));
  }, []);

  return (
    <div>
      <h1>Tasks</h1>

      <ul>
        {tasks.map((task) => (
          <li key={task.id}>{task.title}</li>
        ))}
      </ul>
    </div>
  );
}
