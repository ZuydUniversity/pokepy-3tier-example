import { ICard } from "../lib/definitions";
import styles from "../lib/Card.module.css";
import Badge from "./Badge";
import Button from "./Button";

const Card = ({
  body,
  btn,
  title,
  badge,
  image,
  indicator,
  subtitle,
}: ICard) => {
  return (
    <article className={`stack-lg ${styles.card}`}>
      {indicator && <small className={styles.indicator}>{indicator}</small>}
      {badge && <Badge text={badge.text} filled={badge.filled}></Badge>}
      {image && (
        <img src={image} alt="Loading Image" className={styles.image} />
      )}
      <div className="stack-sm">
        <h3 className={styles.title}>{title}</h3>
        {subtitle && <small className={styles.subtitle}>{subtitle}</small>}
      </div>
      <p className={styles.body}>{body}</p>
      {btn && (
        <Button
          filled={btn.filled}
          type={btn.type}
          text={btn.text}
          href={btn.href}
          icon={btn.icon}
        />
      )}
    </article>
  );
};

export default Card;
