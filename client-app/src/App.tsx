import "./App.scss";
import PndHeader from "./common/components/header/header";
import { DarkTheme, LightTheme } from "./constants/colors";
import PndThemeToggle from "./common/components/them_toggle/theme-toggle";
import PndLeftNav from "./componenets/left-nav/left-nav";
import { RouterProvider } from "react-router";
import { router } from "./pages/router";

function App() {

  return (
    <div className="App">
      <PndHeader
        Title="Dev Journal"
        SubTitle="Preston Harms"
        IconPath="img/rd_pnd_2025_rd_128.png"
      >
        <PndThemeToggle DarkTheme={DarkTheme} LightTheme={LightTheme} />
      </PndHeader>
      <div className="pnd-body">
        <div className="pnd-left-nav-container">
          <PndLeftNav/>
        </div>
        <div className="pnd-main-content">
              <RouterProvider router={router} />
        </div>
      </div>
    </div>
  );
}

export default App;
