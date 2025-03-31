import React from 'react';
import Image from 'next/image';

const Navbar = () => {
    return (
        <nav>
            <div>
                <div>
                    <Image src="/logo.png" alt='' width={50} height={50} />
                    <p>Not Brain Found</p>
                </div>
                <ul>
                    <li><a href="">Home</a></li>
                    <li><a href="">About</a></li>
                    <li><a href="">Projects</a></li>
                    <li><a href="">Services</a></li>
                    <li><a href="">Developers</a></li>
                    <li><a href="">Contact</a></li>
                </ul>
                <button>Let&apos;s connect</button>
            </div>
        </nav>
    );
};

export default Navbar;
