import React, { FC } from "react";
import { FieldForm } from "./form/Form";

interface LayoutProps {}

const Layout: FC<LayoutProps> = () => {
  return (
    <div className="flex justify-center">
      <div className="w-3/5">
        <div className="pb-4">
          <h1 className="text-2xl">JutsuClip</h1>
          <p>Unleash the power of seamless productivity with JutsuClip!</p>
        </div>
        <FieldForm />
      </div>
    </div>
  );
};

export default Layout;
