export const getTasks = async () => {
  const res = await fetch("/tasks");
  return res.json();
};

export const createTask = async (task: any) => {
  await fetch("/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(task)
  });
};
