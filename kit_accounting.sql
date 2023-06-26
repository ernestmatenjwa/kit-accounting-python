-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2023 at 01:56 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kit_accounting`
--

-- --------------------------------------------------------

--
-- Table structure for table `business`
--

CREATE TABLE `business` (
  `id` int(30) NOT NULL,
  `c_name` varchar(50) NOT NULL,
  `c_phone` varchar(13) NOT NULL,
  `c_email` varchar(50) NOT NULL,
  `c_postal` varchar(50) NOT NULL,
  `c_physicalAd` varchar(50) NOT NULL,
  `c_slogan` varchar(50) NOT NULL,
  `c_fax_no` varchar(13) NOT NULL,
  `password` varchar(50) NOT NULL,
  `_On` varchar(50) NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `business`
--

INSERT INTO `business` (`id`, `c_name`, `c_phone`, `c_email`, `c_postal`, `c_physicalAd`, `c_slogan`, `c_fax_no`, `password`, `_On`) VALUES
(1, 'eKhonnector', '0725445586', 'khonnect@12', 'Riverside', 'Mbombela', 'Good staff', '07255412', '123', '2023-06-23 15:36:20'),
(2, 'Kayise IT', '0729475467', 'kayise.com', 'Mbombela', 'Mbombela2', 'Good staff', '072554256', '123', '2023-06-26 13:10:23'),
(3, 'Kayise ITT', '074761677', 'kayise@com', '1203', 'Matsulu', 'we serve', '0725641485', '123', '2023-06-26 13:25:25'),
(4, 'Langa Mall', '07254154558', 'langa@com', 'Matsulu', 'Mall', 'Langa', 'we do', '123', '2023-06-26 13:27:33');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `business`
--
ALTER TABLE `business`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `business`
--
ALTER TABLE `business`
  MODIFY `id` int(30) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
