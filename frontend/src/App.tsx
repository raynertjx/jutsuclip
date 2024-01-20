import React, { useEffect, useState, useRef } from 'react';
import Webcam from "react-webcam";

const WebcamCapture = () => {
    const webcamRef = useRef(null);
    const [result, setResult] = useState('');

    const capture = React.useCallback(() => {
        const imageSrc = webcamRef.current.getScreenshot();
        const imageData = imageSrc.split(',')[1];
        fetch('http://localhost:5001/process_image', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ image: imageData})
        })
        .then(response => response.json())
        .then(data => setResult(data.totalFingers))
        .catch(err => console.error(err));
    }, [webcamRef]);

    useEffect(() => {
        const interval = setInterval(() => {
            capture();
        }, 1000);
        return () => clearInterval(interval);
    }, [capture]);

    return (
        <>
            <Webcam
                audio={false}
                height={720}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                width={1280}
            />
            <p>Detected Fingers: {result}</p>
        </>
    );
};

export default WebcamCapture;
