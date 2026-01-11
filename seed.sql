-- Admin user (senha mock apenas para sandbox)
INSERT INTO admin_users (id, username, password_hash, role)
VALUES (1, 'admin', 'pbkdf2:sha256:150000$mock$mockhash', 'superadmin');

-- Insert example transaction
INSERT INTO transactions (transaction_id, amount, method, token, status)
VALUES ('demo-0001', 10.00, 'pix', null, 'pending');
