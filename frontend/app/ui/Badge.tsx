import { IBadge } from "../lib/definitions";
import styles from "../lib/Badge.module.css";

const Badge = ({ text, filled }: IBadge) => {
  const filledClass = filled ? styles.filled : "";
  return (
    <small className={`${styles.badge} uppercase ${filledClass}`}>{text}</small>
  );
};

export default Badge;
