import React from "react";
import "./golbal.css";

export default function Main2() {
  const data = [
    {
      img: "https://help.goabstract.com/hc/theming_assets/01HZH4D4GACXWCRKK6JHQ730XD",
      title: "Using abstract",
      desc: "Abstract lets you manage, version, and document your designs in one place."
    },
    {
      img: "https://help.goabstract.com/hc/theming_assets/01HZH4D45NKFCN3388ZCBJB878",
      title: "Manage Your Account",
      desc: "Configure your account settings, such as your email, profile details, and password."
    },
    {
      img: "https://help.goabstract.com/hc/theming_assets/01HZH4D3M8CRR0C2V5GREVR6HK",
      title: "Manage organizations, teams, and projects",
      desc: "Use Abstract organizations, teams, and projects to organize your people and your work."
    },
    {
      img: "https://help.goabstract.com/hc/theming_assets/01HZH4D38K1S1M9WKWSQZE62YE",
      title: "Managing Bills",
      desc: "Change subscription and payment details."
    },
    {
      img: "https://help.goabstract.com/hc/theming_assets/01HZH4D3S3QY5190TZE3H8ZSVK",
      title: "Authenticate to Abstract",
      desc: "Set up and configure SSO, SCIM, and Just-in-Time provisioning."
    },
    {
      img: "https://help.goabstract.com/hc/theming_assets/01HZH4D3G4S2K93BN3WJPT8600",
      title: "Abstract support",
      desc: "Get in touch with a human."
    }
  ];

  return (
    <div id="main2">
      {data.map((item, index) => (
        <div className="box" key={index}>
          <div className="box-image">
            <img src={item.img} alt={item.title} />
          </div>

          <div className="box-content">
            <h3>{item.title}</h3>
            <br />
            <p>{item.desc}</p>
            <br />
            <a href="#">Learn More →</a>
          </div>
        </div>
      ))}
    </div>
  );
}
