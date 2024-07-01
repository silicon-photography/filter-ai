import React from 'react';
import "./Navbar.css"
import { NavbarData } from './NavbarData';
import FlutterDashIcon from '@mui/icons-material/FlutterDash';

function Navbar() {
  return (
        <div className='navbar'>
            <div className='logo-container'>
                <div id='logo'><FlutterDashIcon/></div>
                <div id='logo-name'>Silicon Photography</div>
            </div>
            <ul className='navbar-list'>
            { NavbarData.map((val, key) => {
                return (
                    <li key={key} className='navbar-row' onClick={() => {window.location.pathname = val.link}}> 
                        <div id='icon'>{val.icon}</div>
                        <div id='title'>{val.title}</div>
                    </li>
                );
            })}
            </ul>
        </div>
  )
}

export default Navbar
