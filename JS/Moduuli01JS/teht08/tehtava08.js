 const startYear = parseInt(prompt("Enter the start year:"));
        const endYear = parseInt(prompt("Enter the end year:"));
        const leapYearsList = document.getElementById("leapYears");

        function isLeapYear(year) {
            return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
        }

        for (let year = startYear; year <= endYear; year++) {
            if (isLeapYear(year)) {
                const listItem = document.createElement("li");
                listItem.textContent = year;
                leapYearsList.appendChild(listItem);
            }
        }