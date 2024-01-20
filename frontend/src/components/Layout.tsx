import React, { FC } from "react";

interface LayoutProps {}

const Layout: FC<LayoutProps> = () => {
  return (
    <div>
      <h1 className="text-2xl">JutsuClip</h1>
      <p>Unleash the power of seamless productivity with JutsuClip!</p>
    </div>
  );
};

export default Layout;
