import React, { FC, useEffect, useRef, useState } from "react";
import Webcam from "react-webcam";
import { Button } from "./ui/button";

interface WebcamProps {
  setIsHome: React.Dispatch<React.SetStateAction<boolean>>;
}

const WebcamCapture: FC<WebcamProps> = ({ setIsHome }) => {
  const webcamRef = useRef(null);
  const [result, setResult] = useState("0");
  const [displayInput, setDisplayInput] = useState("");
  const storedInputs = localStorage.getItem("inputs");
  const capture = React.useCallback(() => {
    const imageSrc = webcamRef.current.getScreenshot();
    const imageData = imageSrc.split(",")[1];
    fetch("http://localhost:5001/process_image", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ image: imageData }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.totalFingers) {
          setResult(data.totalFingers);
        } else {
          setResult("0");
        }
      })
      .catch((err) => console.error(err));
  }, [webcamRef]);
  useEffect(() => {
    if (webcamRef.current) {
      const interval = setInterval(() => {
        capture();
      }, 500);
      return () => clearInterval(interval);
    }
  }, [capture]);

  useEffect(() => {
    if (storedInputs) {
      console.log(result);
      const textToDisplay = JSON.parse(storedInputs).inputs[+result].value;
      setDisplayInput(textToDisplay);
      navigator.clipboard.writeText(textToDisplay);
    } else {
      setDisplayInput("No result stored!");
    }
  }, [result]);
  return (
    <>
      <Button onClick={() => setIsHome(true)} />
      <Webcam
        audio={false}
        height={720}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={1280}
      />{" "}
      <p>Detected Fingers: {result}</p> <p>Text Output: {displayInput}</p>
    </>
  );
};

export default WebcamCapture;
