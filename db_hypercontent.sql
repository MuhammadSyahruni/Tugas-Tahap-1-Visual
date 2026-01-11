-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 11, 2026 at 05:12 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_hypercontent`
--

-- --------------------------------------------------------

--
-- Table structure for table `hyperlink`
--

CREATE TABLE `hyperlink` (
  `id` int(11) NOT NULL,
  `id_materi` int(11) NOT NULL,
  `label_link` varchar(255) NOT NULL,
  `url_video` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `hyperlink`
--

INSERT INTO `hyperlink` (`id`, `id_materi`, `label_link`, `url_video`) VALUES
(1, 1, 'aaa', 'aaaa'),
(2, 1, 'bhhhv', 'gg');

-- --------------------------------------------------------

--
-- Table structure for table `materi`
--

CREATE TABLE `materi` (
  `id` int(11) NOT NULL,
  `id_subtema` int(11) NOT NULL,
  `judul` varchar(255) NOT NULL,
  `isi_materi` text DEFAULT NULL,
  `halaman` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `materi`
--

INSERT INTO `materi` (`id`, `id_subtema`, `judul`, `isi_materi`, `halaman`) VALUES
(1, 1, 'apa', 'ahu', 10),
(7, 6, 'h', 'ooo', 5);

-- --------------------------------------------------------

--
-- Table structure for table `sub_tema`
--

CREATE TABLE `sub_tema` (
  `id` int(11) NOT NULL,
  `nama_sub_tema` varchar(255) NOT NULL,
  `deskripsi` text DEFAULT NULL,
  `urutan` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `sub_tema`
--

INSERT INTO `sub_tema` (`id`, `nama_sub_tema`, `deskripsi`, `urutan`) VALUES
(1, 'Retorika', 'Pidato', 1),
(6, 't', 'y', 2);

-- --------------------------------------------------------

--
-- Table structure for table `validasi`
--

CREATE TABLE `validasi` (
  `id` int(11) NOT NULL,
  `nama_ahli` varchar(255) NOT NULL,
  `bidang` varchar(100) DEFAULT NULL,
  `skor` int(2) DEFAULT NULL,
  `catatan` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `validasi_ahli`
--

CREATE TABLE `validasi_ahli` (
  `id` int(11) NOT NULL,
  `nama_ahli` varchar(255) DEFAULT NULL,
  `bidang` varchar(100) DEFAULT NULL,
  `skor` int(11) DEFAULT NULL,
  `catatan` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `validasi_ahli`
--

INSERT INTO `validasi_ahli` (`id`, `nama_ahli`, `bidang`, `skor`, `catatan`) VALUES
(1, '8000', 'Ahli Bahasa', 9, 'jjjj'),
(2, '100', 'Ahli Materi', 3, 'bhasbhas'),
(3, '1000', 'Ahli Media', 12, NULL),
(4, '1000', 'Ahli Desain', 10, 'jsdb'),
(5, 'ggcg', 'Ahli Materi', 77, 'gcgc');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `hyperlink`
--
ALTER TABLE `hyperlink`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_link_materi` (`id_materi`);

--
-- Indexes for table `materi`
--
ALTER TABLE `materi`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_materi_subtema` (`id_subtema`);

--
-- Indexes for table `sub_tema`
--
ALTER TABLE `sub_tema`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `validasi`
--
ALTER TABLE `validasi`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `validasi_ahli`
--
ALTER TABLE `validasi_ahli`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hyperlink`
--
ALTER TABLE `hyperlink`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `materi`
--
ALTER TABLE `materi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `sub_tema`
--
ALTER TABLE `sub_tema`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `validasi`
--
ALTER TABLE `validasi`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `validasi_ahli`
--
ALTER TABLE `validasi_ahli`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `hyperlink`
--
ALTER TABLE `hyperlink`
  ADD CONSTRAINT `fk_link_materi` FOREIGN KEY (`id_materi`) REFERENCES `materi` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `materi`
--
ALTER TABLE `materi`
  ADD CONSTRAINT `fk_materi_subtema` FOREIGN KEY (`id_subtema`) REFERENCES `sub_tema` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
