'use client'
import React from 'react'
import { motion } from "motion/react"
import CorvetteCanvas from '../canvas/model';

const bgGradient = () => {
    const bgItems = [
        'linear-gradient(120deg, rgba(33,33,33,1) 0%, rgba(7,63,66,1) 50%, rgba(11,12,16,1) 100%);',
        'linear-gradient(120deg, rgba(33,33,33,1) 0%, rgba(0,241,255,1) 50%, rgba(11,12,16,1) 100%)'
    ]

    return (
        <motion.div
            id='bgGradeint'
            transition={{
                // repeat: Infinity,
                duration: 10,
                ease: 'easeInOut'
            }}
            animate={{
                background: [
                    '#111'
                    // 'radial-gradient(circle, rgba(15,0,50,1) 0%, rgba(17,17,17,1) 100%)',
                    // 'radial-gradient(circle, rgba(15,0,100,1) 0%, rgba(17,17,17,1) 100%)',
                    // 'radial-gradient(circle, rgba(15,0,50,1) 0%, rgba(17,17,17,1) 100%)'
                ]
            }}
            className='w-full h-[100vh] fixed z-0'
        >
        <CorvetteCanvas/>
        </motion.div>
    );
};

export default bgGradient;

