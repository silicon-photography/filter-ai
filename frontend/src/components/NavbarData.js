import React from 'react'
import HomeIcon from '@mui/icons-material/Home';
import AnalyticsIcon from '@mui/icons-material/Analytics';
import EventIcon from '@mui/icons-material/Event';
import PersonIcon from '@mui/icons-material/Person';
import PhotoCameraIcon from '@mui/icons-material/PhotoCamera';
import WhatsAppIcon from '@mui/icons-material/WhatsApp';

export const NavbarData = [
    {
        title: "Home",
        icon: <HomeIcon />,
        link: "/home"
    },
    {
        title: "Dashboard",
        icon: <AnalyticsIcon />,
        link: "/dashboard"
    },
    {
        title: "Calendar",
        icon: <EventIcon />,
        link: "/calendar"
    },
    {
        title: "Customers",
        icon: <PersonIcon />,
        link: "/customers"
    },
    {
        title: "Photo Portal",
        icon: <PhotoCameraIcon />,
        link: "/portal"
    },
    {
        title: "Messages",
        icon: <WhatsAppIcon />,
        link: "/messages"
    }
]