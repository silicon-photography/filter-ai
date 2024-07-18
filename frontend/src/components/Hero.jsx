
import Button from "./Button";
import Section from "./Section";
import { curve, heroBackground, robot } from "../assets";

const Hero = () => {
  return (
  <Section
  className="pt-[3rem] -mt-[5.25]"
  crosses
  crossesOffset="lg:translate-y-[5.25rem]"
  customPaddings
  id="hero"
  
  >
    <div className="container relative">
        <div className="relative z-1 max-w-[62rem]
        mx-auto text-center mb-[4rem] md:mb-20 lg:mb:[6rem]">
            <h1 className="h1 mb-6">
            Edit your Photos Faster with 
                <span className="inline-block relative"> 
                camerAI{" "} 
                <img 
                    src={curve}
                    className="absolute top-full left-0 w-full xl:-mt-2"
                    width={624}
                    height={28}
                    alt="Curve"
                />
                </span>
            </h1>
            <p className="body-1 max-w-3xl mx-auto mb-6
            text-n-2 lg:mb-8"> 
            Unleash the power of AI onto your post-production workflow
            </p>
            <Button href="/pricing" white>
                Get Started
            </Button>
        </div>

    </div>
    </Section>
  );

};

export default Hero;
