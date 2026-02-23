import { IButton } from "../lib/definitions";
import styles from "../lib/Button.module.css";

const Button = ({ text, filled, type, href, icon }: IButton) => {
  const filledClass = filled ? styles.filled : "";
  return (
    <a
      href={href}
      className={`${styles.btn} ${styles[type.toLowerCase()]} ${filledClass}`}
    >
      <span>{text}</span>
      {icon}
    </a>
  );
};

export default Button;
