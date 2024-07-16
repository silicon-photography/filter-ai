import camerAI from "../assets/camerAI.png"; 

const Header = () => {
    return (
        //create a fixed header that stays at the top of the page
      <div className="fixed top-0 z-50 bg-n-8/90 backdrop-blur-sm border-b
      border-n-6 lg:bg-n-8/90 lg:backdrop-blur-sm">
        <div className="flex items-center px-5 lg:px-7.5 xl:px-10
        max-lg:py-4">
            <a className="block w-[12rem] xl:mr-8" href="#hero"> 
            <img src={camerAI} width={190} height={40} alt="CamerAI Logo" />
            </a>
        </div>
      </div>
    );
  };
  
export default Header;
