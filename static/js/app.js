const themeToggle = document.getElementById("themeToggle");

const savedTheme = localStorage.getItem("theme");

if (savedTheme === "dark") {
    document.body.classList.add("dark-mode");

    if (themeToggle) {
        themeToggle.textContent = "☀️";
    }
}

if (themeToggle) {

    themeToggle.addEventListener("click", () => {

        document.body.classList.toggle("dark-mode");

        const isDark =
            document.body.classList.contains("dark-mode");

        if (isDark) {

            themeToggle.textContent = "☀️";
            localStorage.setItem("theme", "dark");

        } else {

            themeToggle.textContent = "🌙";
            localStorage.setItem("theme", "light");

        }

    });

}


// ================================
// LOGIN
// ================================

const loginForm =
    document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener(
        "submit",
        async function (e) {

            e.preventDefault();

            const username =
                document.getElementById("username")
                    .value.trim();

            const password =
                document.getElementById("password")
                    .value;

            const message =
                document.getElementById("loginMessage");

            const button =
                loginForm.querySelector(".auth-submit");

            message.style.display = "none";

            button.disabled = true;
            button.innerHTML = "Logging in...";


            try {

                const response = await fetch(
                    "/api/token/",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            username: username,
                            password: password
                        })
                    }
                );


                const data =
                    await response.json();

                if (response.ok) {

                    localStorage.setItem(
                        "access_token",
                        data.access
                    );

                    localStorage.setItem(
                        "refresh_token",
                        data.refresh
                    );


                    message.style.display =
                        "block";

                    message.style.color =
                        "#22c55e";

                    message.innerHTML =
                        "✓ Login successful!";


                    // Get logged-in user's role
                    try {

                        const profileResponse =
                            await fetch(
                                "/api/auth/profile/",
                                {
                                    method: "GET",

                                    headers: {
                                        "Authorization":
                                            "Bearer " + data.access
                                    }
                                }
                            );


                        if (!profileResponse.ok) {

                            throw new Error(
                                "Unable to load user profile"
                            );

                        }


                        const user =
                            await profileResponse.json();


                        console.log(
                            "Logged-in user:",
                            user
                        );


                        setTimeout(() => {

                            if (user.role === "EMPLOYER") {

                                window.location.href =
                                    "/employer-dashboard/";

                            } else {

                                window.location.href =
                                    "/jobs/";

                            }

                        }, 800);


                    } catch (error) {

                        console.error(
                            "Role detection error:",
                            error
                        );


                        message.style.color =
                            "#ef4444";

                        message.innerHTML =
                            "✕ Unable to load user profile.";

                        button.disabled = false;

                        button.innerHTML =
                            'Login <span>→</span>';

                    }
                    
            } else {

                message.style.display =
                    "block";

                message.style.color =
                    "#ef4444";


                if (data.detail) {

                    message.innerHTML =
                        "✕ " + data.detail;

                } else {

                    message.innerHTML =
                        "✕ Invalid username or password.";

                }


                button.disabled = false;

                button.innerHTML =
                    'Login <span>→</span>';
            }


        } catch (error) {

            console.error(
                "Login error:",
                error
            );


            message.style.display =
                "block";

            message.style.color =
                "#ef4444";

            message.innerHTML =
                "✕ Unable to connect to server.";


            button.disabled = false;

            button.innerHTML =
                'Login <span>→</span>';
        }

}
    );

}


// ================================
// LOAD LOGGED-IN USER PROFILE
// ================================

async function loadUserProfile() {

    const accessToken =
        localStorage.getItem("access_token");


    if (!accessToken) {
        return;
    }


    try {

        const response =
            await fetch(
                "/api/auth/profile/",
                {
                    method: "GET",

                    headers: {
                        "Authorization":
                            "Bearer " + accessToken
                    }
                }
            );


        if (!response.ok) {

            console.log(
                "Unable to load profile"
            );

            return;
        }


        const user =
            await response.json();


        console.log(
            "Logged-in user:",
            user
        );


    } catch (error) {

        console.error(
            "Profile error:",
            error
        );

    }

}

loadUserProfile();


// ================================
// LOAD JOBS
// ================================

async function loadJobs() {

    const jobsContainer =
        document.getElementById(
            "jobs-container"
        );


    if (!jobsContainer) {
        return;
    }


    try {

        const response =
            await fetch("/api/jobs/");


        const jobs =
            await response.json();


        if (!response.ok) {

            jobsContainer.innerHTML = `
                <p>Unable to load jobs.</p>
            `;

            return;
        }


        const jobsCount =
            document.getElementById(
                "jobsCount"
            );


        if (jobsCount) {

            jobsCount.textContent =
                jobs.length;

        }


        if (jobs.length === 0) {

            jobsContainer.innerHTML = `

                <div class="empty-jobs">

                    <div>💼</div>

                    <h3>
                        No jobs available
                    </h3>

                    <p>
                        New opportunities will
                        appear here soon.
                    </p>

                </div>

            `;

            return;
        }


        jobsContainer.innerHTML =
            jobs.map(job => `

                <div class="job-card">

                    <div class="job-card-top">

                        <div class="job-icon">
                            💼
                        </div>

                        <span class="job-type">
                            ${job.job_type}
                        </span>

                    </div>


                    <h2>
                        ${job.title}
                    </h2>


                    <h4>
                        ${job.company}
                    </h4>


                    <p class="job-location">
                        📍 ${job.location}
                    </p>


                    <p class="job-description">
                        ${job.description}
                    </p>


                    <div class="job-card-bottom">

                        <span>
                            💰
                            ${job.salary ??
                "Not specified"}
                        </span>


                        <a href="/jobs/${job.id}/">
                            View Job →
                        </a>

                    </div>

                </div>

            `).join("");


    } catch (error) {

        console.error(
            "Jobs error:",
            error
        );


        jobsContainer.innerHTML = `
            <p>
                Unable to connect to server.
            </p>
        `;
    }

}

loadJobs();


// ================================
// LOAD JOB DETAILS
// ================================

async function loadJobDetails() {

    const container =
        document.getElementById(
            "job-detail-container"
        );


    if (!container) {
        return;
    }


    const pathParts =
        window.location.pathname
            .split("/")
            .filter(Boolean);


    const jobId =
        pathParts[pathParts.length - 1];


    try {

        const response =
            await fetch(
                `/api/jobs/${jobId}/`
            );


        const job =
            await response.json();


        if (!response.ok) {

            container.innerHTML = `

                <div class="job-error">

                    <h2>
                        Job not found
                    </h2>

                    <p>
                        Sorry, this job is
                        no longer available.
                    </p>

                    <a href="/jobs/">
                        ← Back to Jobs
                    </a>

                </div>

            `;

            return;
        }


        // ================================
        // JOB DETAILS HTML
        // ================================

        container.innerHTML = `

            <div class="job-detail-card">


                <a
                    href="/jobs/"
                    class="back-link"
                >
                    ← Back to Jobs
                </a>


                <div class="job-detail-header">


                    <div class="job-detail-icon">
                        💼
                    </div>


                    <div>

                        <span class="job-detail-type">
                            ${job.job_type}
                        </span>


                        <h1>
                            ${job.title}
                        </h1>


                        <h3>
                            ${job.company}
                        </h3>


                        <p>
                            📍 ${job.location}
                        </p>

                    </div>

                </div>


                <div class="job-detail-meta">


                    <div>

                        <span>
                            💰 Salary
                        </span>

                        <strong>
                            ${job.salary ??
            "Not specified"}
                        </strong>

                    </div>


                    <div>

                        <span>
                            🏢 Company
                        </span>

                        <strong>
                            ${job.company}
                        </strong>

                    </div>


                    <div>

                        <span>
                            💼 Job Type
                        </span>

                        <strong>
                            ${job.job_type}
                        </strong>

                    </div>


                </div>


                <div class="job-detail-content">


                    <div class="job-main-content">


                        <h2>
                            About this job
                        </h2>


                        <p>
                            ${job.description}
                        </p>


                        <h2>
                            Requirements
                        </h2>


                        <p>
                            ${job.requirements}
                        </p>


                    </div>


                    <!-- APPLY CARD -->

                    <aside class="job-apply-card">


                        <h3>
                            Apply for this job
                        </h3>


                        <p>
                            Take the next step
                            in your career.
                        </p>


                        <form id="applyForm">


                            <div class="form-group">

                                <label for="resume">
                                    Resume
                                </label>


                                <input
                                    type="file"
                                    id="resume"
                                    name="resume"
                                    accept=".pdf,.doc,.docx"
                                    required
                                >

                            </div>


                            <div class="form-group">

                                <label for="cover_letter">
                                    Cover Letter
                                </label>


                                <textarea
                                    id="cover_letter"
                                    name="cover_letter"
                                    rows="6"
                                    placeholder="Write your cover letter..."
                                    required
                                ></textarea>

                            </div>


                            <button
                                type="submit"
                                class="apply-btn"
                            >
                                Submit Application →
                            </button>


                        </form>


                    </aside>


                </div>


            </div>

        `;


        // ================================
        // APPLY FORM SUBMIT
        // ================================

        const applyForm =
            document.getElementById(
                "applyForm"
            );


        if (applyForm) {

            applyForm.addEventListener(
                "submit",
                async function (e) {

                    e.preventDefault();


                    console.log(
                        "Apply form submitted"
                    );


                    const accessToken =
                        localStorage.getItem(
                            "access_token"
                        );


                    if (!accessToken) {

                        alert(
                            "Please login as a candidate to apply."
                        );

                        window.location.href =
                            "/login/";

                        return;
                    }


                    const resumeInput =
                        document.getElementById(
                            "resume"
                        );


                    const coverLetterInput =
                        document.getElementById(
                            "cover_letter"
                        );


                    const resume =
                        resumeInput.files[0];


                    const coverLetter =
                        coverLetterInput.value.trim();


                    if (!resume) {

                        alert(
                            "Please upload your resume."
                        );

                        return;
                    }


                    if (!coverLetter) {

                        alert(
                            "Please write a cover letter."
                        );

                        return;
                    }


                    // ================================
                    // FORM DATA
                    // ================================

                    const formData =
                        new FormData();


                    formData.append(
                        "job",
                        job.id
                    );


                    formData.append(
                        "resume",
                        resume
                    );


                    formData.append(
                        "cover_letter",
                        coverLetter
                    );


                    const button =
                        applyForm.querySelector(
                            ".apply-btn"
                        );


                    button.disabled = true;

                    button.textContent =
                        "Submitting...";


                    try {

                        const response =
                            await fetch(
                                "/api/applications/",
                                {
                                    method: "POST",

                                    headers: {
                                        "Authorization":
                                            "Bearer " +
                                            accessToken
                                    },

                                    body: formData
                                }
                            );


                        // IMPORTANT:
                        // Response ko text ke form mein
                        // read kar rahe hain.

                        const responseText =
                            await response.text();


                        console.log(
                            "Application status:",
                            response.status
                        );


                        console.log(
                            "Application response:",
                            responseText
                        );


                        let data = {};


                        if (responseText) {

                            try {

                                data =
                                    JSON.parse(
                                        responseText
                                    );

                            } catch (error) {

                                console.log(
                                    "Response is not JSON"
                                );

                            }

                        }


                        // ================================
                        // SUCCESS
                        // ================================

                        if (response.ok) {

                            alert(
                                "🎉 Application submitted successfully!"
                            );


                            button.textContent =
                                "✓ Application Submitted";


                            button.disabled =
                                true;


                            applyForm.reset();


                        }

                        // ================================
                        // ERROR
                        // ================================

                        else {

                            console.error(
                                "Application error:",
                                data
                            );


                            button.disabled =
                                false;


                            button.textContent =
                                "Submit Application →";


                            if (data.resume) {

                                alert(
                                    "Resume: " +
                                    data.resume[0]
                                );

                            }

                            else if (
                                data.cover_letter
                            ) {

                                alert(
                                    "Cover Letter: " +
                                    data.cover_letter[0]
                                );

                            }

                            else if (data.job) {

                                alert(
                                    "Job: " +
                                    data.job[0]
                                );

                            }

                            else if (data.detail) {

                                alert(
                                    data.detail
                                );

                            }

                            else {

                                alert(
                                    "Unable to submit application."
                                );

                            }

                        }


                    } catch (error) {

                        console.error(
                            "Application error:",
                            error
                        );


                        button.disabled =
                            false;


                        button.textContent =
                            "Submit Application →";


                        alert(
                            "Unable to connect to server."
                        );

                    }

                }
            );

        }


    } catch (error) {

        console.error(
            "Job details error:",
            error
        );


        container.innerHTML = `

            <div class="job-error">

                <h2>
                    Unable to load job
                </h2>

                <p>
                    Please try again later.
                </p>

            </div>

        `;
    }

}

loadJobDetails();


// ================================
// MY APPLICATIONS
// ================================

async function loadMyApplications() {

    const container =
        document.getElementById(
            "applications-container"
        );


    if (!container) {
        return;
    }


    const accessToken =
        localStorage.getItem(
            "access_token"
        );


    if (!accessToken) {

        container.innerHTML = `

            <div class="application-message">

                <h2>
                    Please Login
                </h2>

                <p>
                    Login as a candidate
                    to view your applications.
                </p>


                <a
                    href="/login/"
                    class="primary-btn"
                >
                    Login →
                </a>

            </div>

        `;

        return;
    }


    try {

        const response =
            await fetch(
                "/api/applications/my-applications/",
                {
                    method: "GET",

                    headers: {
                        "Authorization":
                            "Bearer " + accessToken
                    }
                }
            );


        const applications =
            await response.json();


        console.log(
            "My applications:",
            applications
        );


        if (!response.ok) {

            container.innerHTML = `

                <div class="application-message">

                    <h2>
                        Unable to load applications
                    </h2>

                    <p>
                        Please login again and try.
                    </p>

                </div>

            `;

            return;
        }


        const applicationsCount =
            document.getElementById(
                "applicationsCount"
            );


        if (applicationsCount) {

            applicationsCount.textContent =
                applications.length;

        }


        if (applications.length === 0) {

            container.innerHTML = `

                <div class="application-message">

                    <div class="empty-icon">
                        📄
                    </div>

                    <h2>
                        No Applications Yet
                    </h2>

                    <p>
                        You haven't applied for
                        any jobs yet.
                    </p>


                    <a
                        href="/jobs/"
                        class="primary-btn"
                    >
                        Find Jobs →
                    </a>

                </div>

            `;

            return;
        }


        container.innerHTML =
            applications.map(
                application => `

                    <div class="application-card">


                        <div
                            class="application-card-header"
                        >


                            <div
                                class="application-icon"
                            >
                                💼
                            </div>


                            <div>

                                <h2>
                                    ${application.job_title ||
                    "Job Application"
                    }
                                </h2>


                                <p>
                                    ${application.company ||
                    "Company"
                    }
                                </p>

                            </div>


                        </div>


                        <div
                            class="application-info"
                        >


                            <div>

                                <span>
                                    Status
                                </span>


                                <strong
                                    class="application-status"
                                >
                                    ${application.status ||
                    "Applied"
                    }
                                </strong>

                            </div>


                            <div>

                                <span>
                                    Applied On
                                </span>


                                <strong>

                                    ${application.applied_at
                        ? new Date(
                            application.applied_at
                        ).toLocaleDateString()
                        : "N/A"
                    }

                                </strong>

                            </div>


                        </div>


                        <div
                            class="application-footer"
                        >

                            <span>
                                📄 Resume Submitted
                            </span>


                            <span>
                                ✓ Application Sent
                            </span>

                        </div>


                    </div>

                `
            ).join("");


    } catch (error) {

        console.error(
            "My applications error:",
            error
        );


        container.innerHTML = `

            <div class="application-message">

                <h2>
                    Unable to connect
                </h2>

                <p>
                    Please try again later.
                </p>

            </div>

        `;
    }

}

loadMyApplications();

// ================================
// EMPLOYER LOGOUT
// ================================

const employerLogout = document.getElementById("employerLogout");

if (employerLogout) {

    employerLogout.addEventListener("click", function () {

        localStorage.removeItem("access_token");
        localStorage.removeItem("refresh_token");

        window.location.href = "/login/";

    });

}

// // ================================
// // EMPLOYER DASHBOARD
// // ================================

// async function loadEmployerDashboard() {

//     const totalJobs =
//         document.getElementById("totalJobs");

//     const totalApplications =
//         document.getElementById("totalApplications");

//     const activeJobs =
//         document.getElementById("activeJobs");

//     const recentApplications =
//         document.getElementById("recentApplications");


//     // Dashboard page nahi hai
//     if (
//         !totalJobs &&
//         !totalApplications &&
//         !activeJobs &&
//         !recentApplications
//     ) {
//         return;
//     }


//     const accessToken =
//         localStorage.getItem("access_token");


//     // Login nahi hai
//     if (!accessToken) {

//         window.location.href = "/login/";

//         return;
//     }


//     try {

//         const response =
//             await fetch(
//                 "/api/jobs/employer-dashboard/",
//                 {
//                     method: "GET",

//                     headers: {
//                         "Authorization":
//                             "Bearer " + accessToken
//                     }
//                 }
//             );


//         const data =
//             await response.json();


//         console.log(
//             "Employer Dashboard:",
//             data
//         );


//         if (!response.ok) {

//             alert(
//                 data.detail ||
//                 "Unable to load employer dashboard."
//             );

//             return;
//         }


//         // ================================
//         // DASHBOARD COUNTS
//         // ================================

//         if (totalJobs) {

//             totalJobs.textContent =
//                 data.total_jobs;
//         }


//         if (totalApplications) {

//             totalApplications.textContent =
//                 data.total_applications;
//         }


//         if (activeJobs) {

//             activeJobs.textContent =
//                 data.active_jobs;
//         }


//         // ================================
//         // RECENT APPLICATIONS
//         // ================================

//         if (
//             recentApplications &&
//             data.recent_applications
//         ) {

//             if (
//                 data.recent_applications.length === 0
//             ) {

//                 recentApplications.innerHTML = `

//                     <div class="application-message">

//                         <div class="empty-icon">
//                             📄
//                         </div>

//                         <h2>
//                             No applications yet
//                         </h2>

//                         <p>
//                             Applications from candidates
//                             will appear here.
//                         </p>

//                     </div>

//                 `;

//             } else {

//                 recentApplications.innerHTML =
//                     data.recent_applications
//                         .map(application => `

//                             <div class="application-card">

//                                 <div class="application-card-header">

//                                     <div class="application-icon">
//                                         👤
//                                     </div>

//                                     <div>

//                                         <h2>
//                                             ${application.job_title ||
//                             "Job Application"
//                             }
//                                         </h2>

//                                         <p>
//                                             ${application.company ||
//                             "Company"
//                             }
//                                         </p>

//                                     </div>

//                                 </div>


//                                 <div class="application-info">

//                                     <div>

//                                         <span>
//                                             Candidate
//                                         </span>

//                                         <strong>
//                                             ${application.candidate ||
//                             "Unknown"
//                             }
//                                         </strong>

//                                     </div>


//                                     <div>

//                                         <span>
//                                             Status
//                                         </span>

//                                         <strong
//                                             class="application-status"
//                                         >
//                                             ${application.status ||
//                             "Applied"
//                             }
//                                         </strong>

//                                     </div>

//                                 </div>


//                                 <div class="application-footer">

//                                     <span>
//                                         📅 ${application.applied_at
//                                 ? new Date(
//                                     application.applied_at
//                                 ).toLocaleDateString()
//                                 : "N/A"
//                             }
//                                     </span>

//                                     <span>
//                                         ✓ Application Received
//                                     </span>

//                                 </div>

//                             </div>

//                         `)
//                         .join("");
//             }

//         }


//     } catch (error) {

//         console.error(
//             "Employer dashboard error:",
//             error
//         );


//         if (recentApplications) {

//             recentApplications.innerHTML = `

//                 <div class="application-message">

//                     <h2>
//                         Unable to connect
//                     </h2>

//                     <p>
//                         Please try again later.
//                     </p>

//                 </div>

//             `;

//         }

//     }

// }


// loadEmployerDashboard();