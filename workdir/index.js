import React from 'react'; const App = () => {
  const [count, setCount] = React.useState(0);

  return (
    <div>
      <button onClick={() => setCount(count + 1)}>Click me</button>
      <p>Counter: {count}</p>
    </div>
  );
};export default App;