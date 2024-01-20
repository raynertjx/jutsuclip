import React, { FC } from "react";
import FieldForm from "./form/Form";

interface HomeProps {
  setIsHome: React.Dispatch<React.SetStateAction<boolean>>;
}

const Home: FC<HomeProps> = ({ setIsHome }) => {
  return (
    <div className="w-3/5">
      <div className="pb-4">
        <h1 className="text-2xl">JutsuClip</h1>
        <p>Unleash the power of seamless productivity with JutsuClip!</p>
      </div>
      <FieldForm setIsHome={setIsHome} />
    </div>
  );
};

export default Home;
