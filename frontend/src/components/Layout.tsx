import React, { useState, FC } from "react";
import Home from "./Home";
import WebcamCapture from "./Webcam";

interface LayoutProps {}

const Layout: FC<LayoutProps> = () => {
  const [isHome, setIsHome] = useState(true);

  return (
    <div className="flex justify-center">
      {isHome ? (
        <Home setIsHome={setIsHome} />
      ) : (
        <WebcamCapture setIsHome={setIsHome} />
      )}
    </div>
  );
};

export default Layout;
