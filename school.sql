-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 24, 2023 at 06:05 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `school`
--

-- --------------------------------------------------------

--
-- Table structure for table `add_student`
--

CREATE TABLE `add_student` (
  `stu_reg_no` varchar(50) NOT NULL,
  `stu_nm` varchar(50) NOT NULL,
  `stu_dob` varchar(50) NOT NULL,
  `stu_age` varchar(50) NOT NULL,
  `stu_class` varchar(50) NOT NULL,
  `current_date` varchar(50) NOT NULL,
  `stu_address` varchar(50) NOT NULL,
  `stu_gender` varchar(50) NOT NULL,
  `stu_email` varchar(50) NOT NULL,
  `stu_con` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `add_student`
--

INSERT INTO `add_student` (`stu_reg_no`, `stu_nm`, `stu_dob`, `stu_age`, `stu_class`, `current_date`, `stu_address`, `stu_gender`, `stu_email`, `stu_con`) VALUES
('1', 'charmi', '15/11/2008', '18', '9', '', 'upleta,rajkot', 'female', '123@gmail.com', ''),
('2', 'abc', '06-09-2002', '15', '3', '', 'fsd', 'fsd', 'fsdf', '534534'),
('3', 'tina', '02-05-2006', '15', '9', '', 'dasd', 'fe', 'fsdf', '3542343'),
('54', 'gdf', '02-09-200', '15', '5', '', 'gdf', 'g', 'gfd', '435'),
('53', 'fds', '1998-05-02 00:00:00', '25', '4', '', 'tdr', 'dgf', 'gfd', '45'),
('567', 'gf', '2000-06-02 00:00:00', '23', '10', '', 'xcf', 'female', 'gdf', '3534'),
('456', 'gdfg', '1998-05-06 00:00:00', '25', '5', '', 'gdg', 'male', 'gdf', '65436'),
('534', 'fd', '1998-08-06 00:00:00', '25', '5', '', 'fsd', 'male', 'fdsf', '5345'),
('564', 'gf', '02-05-2000', '23', '8', '', 'fdf', 'female', 'fds', '535'),
('122', 'sdsds', '12-03-2004', '25', '9', '', 'xcxc', 'male', 'xcxc', '123232'),
('1222', 'knm,m', '12-12-2003', '19', '8', '', 'dsxsxs', 'male', 'sxscs', '9313786986'),
('111', 'kkjklm', '12-12-2003', '19', '7', '', 'dfdfddfdf', 'male', 'dsdsd', '9313782345'),
('45', 'kjlkl', '02-04-2006', '17', '8', '', 'scdfds', 'male', 'asad', '9876543210'),
('5656', 'sdsde', '15-11-2002', '20', '4', '', 'sdsds', 'male', 'sdsd', '9876543210');

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `stu_reg_no` varchar(50) NOT NULL,
  `stu_nm` varchar(50) NOT NULL,
  `start_date_entry` date NOT NULL,
  `end_date_entry` date NOT NULL,
  `date_range` varchar(50) NOT NULL,
  `present` varchar(50) NOT NULL,
  `absent` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`stu_reg_no`, `stu_nm`, `start_date_entry`, `end_date_entry`, `date_range`, `present`, `absent`) VALUES
('2', 'abc', '2023-08-01', '2023-08-31', '31', '30', '11'),
('1', 'charmi', '2023-08-01', '2023-08-20', '20', '10', '10'),
('4', 'da', '2023-08-08', '2023-08-31', '24', '20', '4'),
('5', 'assd', '2023-08-01', '2023-08-23', '23', '20', '3'),
('567', 'gf', '0000-00-00', '0000-00-00', '32', '30', '2'),
('534', 'fd', '0000-00-00', '0000-00-00', '32', '25', '7');

-- --------------------------------------------------------

--
-- Table structure for table `login`
--

CREATE TABLE `login` (
  `id` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login`
--

INSERT INTO `login` (`id`, `password`) VALUES
('h', '123'),
('d', '12'),
('hh', '1234');

-- --------------------------------------------------------

--
-- Table structure for table `staff_manage`
--

CREATE TABLE `staff_manage` (
  `stff_id` varchar(50) NOT NULL,
  `stff_f_nm` varchar(50) NOT NULL,
  `stff_gen` varchar(50) NOT NULL,
  `stff_age` varchar(50) NOT NULL,
  `stff_desig` varchar(50) NOT NULL,
  `stff_adrss` varchar(50) NOT NULL,
  `stff_phone` varchar(50) NOT NULL,
  `stff_email` varchar(50) NOT NULL,
  `stff_dt_join` varchar(50) NOT NULL,
  `stff_pan` varchar(50) NOT NULL,
  `stff_aadhar` varchar(50) NOT NULL,
  `stff_exp` varchar(50) NOT NULL,
  `stff_edu` varchar(50) NOT NULL,
  `stff_salary` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `staff_manage`
--

INSERT INTO `staff_manage` (`stff_id`, `stff_f_nm`, `stff_gen`, `stff_age`, `stff_desig`, `stff_adrss`, `stff_phone`, `stff_email`, `stff_dt_join`, `stff_pan`, `stff_aadhar`, `stff_exp`, `stff_edu`, `stff_salary`) VALUES
('1001', 'abc', 'female', '26', 'teacher', 'ring road', '256859465', 'abc@gmail.com', '2-09-2015', '155454875465', '456465748975646', '5', 'B.ed', '25000'),
('1002', 'hina', 'male', '45', 'teacher', 'manek chowk', '58465758465', 'xyz@gmail.com', '6-8-2014', '4564856456', '54654321', '5', 'M.ed', '124000'),
('1003', 'mina', 'female', '45', 'teacher', 'sdhjk', '456456546', 'mina@gmail.com', '2-9-2015', '5464564', '45456465', '5', 'B.ed', '124500'),
('23', 'da', 'dsa', 'dsa', 'dsd', 'ds', 'ds', 'ds', 'das', 'ds', 'ds', 'sd', 'sda', 'sda');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
