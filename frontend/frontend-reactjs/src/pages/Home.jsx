import React, { useEffect } from "react";

const color = [
  "#E74C3C",
  "#83F523",
  "#ECF523",
  "#F54923",
  "#7A23F5",
  "#23DDF5",
  "#F0F3F4",
  "#48C9B0",
  "#F7F9F9",
  "#E74C3C",
  "#48C9B0",
];

const Home = (props) => {
  useEffect(() => {
    document.title = "UseLess";
    let item = document.getElementById("title");
    let randomColor = Math.floor(Math.random() * color.length);
    item.style.color = color[randomColor];
  }, []);

  return (
    <h1 className="front" id="title">
      Welcome to Useless-Project
    </h1>
  );
};
export default Home;
